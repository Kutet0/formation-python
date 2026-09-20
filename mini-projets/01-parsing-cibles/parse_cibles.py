def ligne_vers_cible(ligne):
    ip, port = ligne.strip().split(":")
    cible = {"IP": ip, "PORT": int(port)}
    return cible

with open("cibles.txt", encoding="utf-8") as file:
    cibles = [ligne_vers_cible(ligne) for ligne in file if ligne.strip() and not ligne.strip().startswith("#")]

ips = {c["IP"] for c in cibles}
count = {ip : sum(1 for c in cibles if c["IP"] == ip) for ip in ips}
print(count)

for cible in cibles:
    print(f"{cible['IP']} -> {cible['PORT']}")