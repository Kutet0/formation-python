def ligne_vers_cible(ligne):
    ip, port = ligne.strip().split(":")
    cible = {"IP": ip, "PORT": int(port)}
    return cible


with open("cibles.txt", encoding="utf-8") as f:
    cibles = [ligne_vers_cible(l) for l in f]

for cible in cibles:
    print(f"{cible['IP']} -> {cible['PORT']}")