liste_cibles = []
with open("cibles.txt", encoding="utf-8") as f:
    for ligne in f:
        morceaux = ligne.strip().split(":")
        ip = morceaux[0]
        port = int(morceaux[1])
        cible = {"IP": ip, "PORT": port}
        liste_cibles.append(cible)

for cible in liste_cibles:
    print(f"{cible["IP"]} -> {cible["PORT"]}")