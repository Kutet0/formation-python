import json
import csv

def sauver_json(cibles, chemin):
    with open("resultats.json", "w", encoding="utf_8") as file:
        json.dump(cibles, file,indent=2,ensure_ascii=False)
    return

def charger_json(chemin):
    with open("resultats.json", encoding="utf_8") as file:
        donnee = json.load(file)
    return donnee

def sauver_csv(cibles, chemin):
    with open("resultat.csv", "w",newline="", encoding="utf_8") as file:
        writer = csv.DictWriter(file, fieldnames=["IP","PORT"])
        writer.writeheader()
        writer.writerows(cibles)

cibles = [{"IP": "10.0.0.5", "PORT": 22}, {"IP": "10.0.0.5", "PORT": 80}]

sauver_json(cibles, "resultats.json")

recharge = charger_json("resultats.json")
print(recharge == cibles)

sauver_csv(cibles, "resultats.csv")