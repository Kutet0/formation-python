def ligne_vers_cible(ligne):
    ip, port = ligne.strip().split(":")
    cible = {"IP": ip, "PORT": int(port)}
    return cible

with open("cibles.txt", encoding="utf-8") as f:
    cibles = [ligne_vers_cible(l) for l in f if l.strip() and not l.strip().startswith("#")]

ips = {c["IP"] for c in cibles}
count = {ip : sum(1 for c in cibles if c["IP"] == ip) for ip in ips}
print(count)

for cible in cibles:
    print(f"{cible['IP']} -> {cible['PORT']}")