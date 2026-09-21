class Cible:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
    
    def adresse(self):
        return f"{self.ip}:{self.port}"
    
    def __repr__(self):
            return f"Cible({self.ip}:{self.port})"
    
    def __eq__(self, autre):
        return self.ip == autre.ip and self.port == autre.port
    
class Resultat:
    def __init__(self, cible, status):
        self.cible = cible
        self.status = status
    
    def __repr__(self):
        return f"{self.cible.adresse()} [{self.status}]"

class Rapport:
    def __init__(self):
        self.resultats = []

    def __len__(self):
        return len(self.resultats)
    
    def ajouter(self, resultat):
        self.resultats.append(resultat)

    def nb_ouverts(self):
        return sum(1 for r in self.resultats if r.status == "ouvert")
    
    def resume(self):
        return f"{len(self)} resultat(s), {self.nb_ouverts()} ouvert(s)"
    
rapport = Rapport()
rapport.ajouter(Resultat(Cible("10.0.0.5", 22), "ouvert"))
rapport.ajouter(Resultat(Cible("10.0.0.5", 80), "ouvert"))
rapport.ajouter(Resultat(Cible("10.0.0.5", 3306), "ferme"))

print(rapport.resultats)
print(rapport.nb_ouverts())
print(rapport.resume())

r1 = Rapport()
r2 = Rapport()
r1.ajouter(Resultat(Cible("1.1.1.1", 22), "ouvert"))
print(len(r1.resultats), len(r2.resultats))