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

def ping(ip, timeout=1.0, count=1):
    if platform.system().lower() == 'windows':
        command = ['ping', '-n', str(count), '-w', str(int(timeout * 1000)), str(ip)]
    else:
        command = ['ping', '-c', str(count), '-W', str(max(1, int(timeout))), str(ip)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return result.returncode == 0 and b"ttl=" in result.stdout.lower()

def ports_scanner(ip, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            code = s.connect_ex((ip, port))
        except socket.timeout:
            return "filtré"
        except socket.gaierror:
            return "hôte injoignable"
        except OSError:
            return "erreur réseau"
        return "ouvert" if code == 0 else "fermé"
        

def machine_up(sous_reseau, timeout,max_worker=100):
    reseau = ipaddress.ip_network(sous_reseau)
    machines = []

    print("_______________________________________________________________")
    print(f"Adresse réseau :                    {reseau.network_address}")
    print(f"Masque de sous-réseau :             {reseau.netmask}")
    print(f"Adresse de diffusion (broadcast) :  {reseau.broadcast_address}")
    print(f"Nombre total d'hôtes utilisables :  {reseau.num_addresses - 2}")
    print("_______________________________________________________________")

    with ThreadPoolExecutor(max_workers=max_worker) as executor:
        futurs = {executor.submit(ping, ip, timeout): ip for ip in reseau.hosts()}
        for futur in as_completed(futurs):
            adresse = futurs[futur]
            if futur.result() == True:
                machines.append(str(adresse))
    return machines

def scan_parallele(ip, ports, timeout, max_worker=100):
    ouvert = []
    with ThreadPoolExecutor(max_workers=max_worker) as executor:
        futurs = {executor.submit(ports_scanner, ip, p, timeout): p for p in ports}
        for futur in as_completed(futurs):
            port = futurs[futur]
            if futur.result() == "ouvert":
                ouvert.append(port)
    return sorted(ouvert)

def plage_ports(debut, fin):
    port = debut
    while port <= fin:
        yield port
        port += 1

commande = args_parse()
machines = machine_up(commande["sous_reseau"], commande["timeout"])

p_debut, p_fin = commande["ports"].strip().split("-")

sauv = []
for ip in machines:
    ouvert = scan_parallele(str(ip), list(plage_ports(int(p_debut), int(p_fin))), commande["timeout"])
    sauv.append({"ip": ip, "port": ouvert})
print(sauv)