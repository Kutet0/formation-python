import socket

def etat_port(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            try:
                code = s.connect_ex((ip, port))
            except socket.timeout:
                return "filtré"
            except socket.gaierror:
                return "hôte injoignable"
            except OSError:
                "erreur réseau"
            return "ouvert" if code == 0 else "fermé"

def plage_ports(debut, fin):
    port = debut
    while port <= fin:
        yield port
        port += 1

print(etat_port("127.0.0.1", 8080))
print(etat_port("127.0.0.1", 9999))
print(etat_port("machin.invalide.xyz", 80))

for p in plage_ports(8078, 8082):
    etat = etat_port("127.0.0.1", p)
    if etat == "ouvert":
        print(f"port {p} : {etat}")