def toutes_cibles(ips, ports):
    couple = [(ip, port) for ip in ips for port in ports]
    return couple

def classer_ports(ports):
    connu = {port: ("bien connu" if port < 1024 else "haut") for port in ports}
    return connu

def aplatir(listes):
    plat = [x for sous_liste in listes for x in sous_liste]
    return plat


print(toutes_cibles(["10.0.0.5", "10.0.0.6"], [22, 80]))

print(classer_ports([22, 8080, 443]))

print(aplatir([[1, 2], [3, 4], [5]]))