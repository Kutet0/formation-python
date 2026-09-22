from concurrent.futures import ThreadPoolExecutor, as_completed
import socket, time

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
                return "erreur réseau"
            return "ouvert" if code == 0 else "fermé"

def plage_ports(debut, fin):
    port = debut
    while port <= fin:
        yield port
        port += 1

def scan_parallele(ip, ports, timeout=1, max_workers=100):
    ouvert = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futurs = {executor.submit(etat_port, ip, p, timeout): p for p in ports}
        for futur in futurs:
            port = futurs[futur]
            if futur.result() == "ouvert":
                ouvert.append(port)
    return sorted(ouvert)

ports = list(plage_ports(8000, 8100))
print(scan_parallele("127.0.0.1", ports))

debut = time.time()
ouverts = scan_parallele("127.0.0.1", list(plage_ports(1, 1000)))
print(f"{ouverts} en {time.time()-debut:.2f}s")
