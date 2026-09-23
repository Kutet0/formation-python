from concurrent.futures import ThreadPoolExecutor, as_completed
import socket, time, argparse, ipaddress, platform, subprocess

def args_parse():
    parse = argparse.ArgumentParser(description="Cartographie de sous réseau")
    parse.add_argument("sous_reseau", help="adresse réseau a scanner")
    parse.add_argument("--ports", default="1-100", help="Plage, ex: 1-100")
    parse.add_argument("--timeout", type=float, default=1.0)
    parse.add_argument("--verbose", action="store_true")
    args = parse.parse_args()
    commande = {"sous_reseau": args.sous_reseau, "ports": args.ports, "timeout": args.timeout, "verbose": args.verbose}
    return commande

def ping(ip, count=4):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), str(ip)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return result.returncode == 0 and b"ttl=" in result.stdout.lower()

def ports_scanner():
    pass

def machine_up(sous_reseau, timeout, max_worker=100):
    reseau = ipaddress.ip_network(sous_reseau)
    machine = []

    print(f"Adresse réseau :                    {reseau.network_address}")
    print(f"Masque de sous-réseau :             {reseau.netmask}")
    print(f"Adresse de diffusion (broadcast) :  {reseau.broadcast_address}")
    print(f"Nombre total d'hôtes utilisables :  {reseau.num_addresses - 2}")

    with ThreadPoolExecutor(max_workers=max_worker) as executor:
        futurs = {executor.submit(ping, ip): ip for ip in reseau.hosts()}
        for futur in as_completed(futurs):
            adresse = futurs[futur]
            if futur.result() == True:
                machine.append(str(adresse))
    return machine

commande = args_parse()
machine = machine_up(commande["sous_reseau"], commande["timeout"])