class Connexion:
    def __init__(self, cible):
        self.cible = cible

    def __enter__(self):
        print(f"connexion a {self.cible}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"fermeture de {self.cible}")
    
with Connexion("10.0.0.1") as c:
    print(f"scan de {c.cible}")

try:
    with Connexion("10.0.0.6") as c:
        print("avant l'erreur")
        raise ValueError("boum")
except ValueError:
    print("erreur attrapée dehors")