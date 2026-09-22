import sys

def plage_ports(debut, fin):
    port = debut
    while port <= fin:
        yield port
        port += 1

def ips_sous_reseau(prefix, debut, fin):
    p = debut
    while p <= fin:
        adr = [prefix, str(p)]
        adresse = ".".join(adr)
        yield adresse
        p += 1

print(list(plage_ports(20,23)))

for ip in ips_sous_reseau("192.168.1", 1, 3):
    print(ip)

g = plage_ports(1, 1000000)
print(type(g))
print(sys.getsizeof(g) < 500)

h = plage_ports(1, 3)    
print(list(h))
print(list(h)) 