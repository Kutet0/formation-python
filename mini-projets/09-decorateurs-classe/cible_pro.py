class Cible:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
    
    @classmethod
    def depuis_texte(cls, texte):
        ip, port = texte.strip().split(":")
        return cls(ip, int(port))
    
    @staticmethod
    def port_valide(port):
         return 0 <= port <= 65535

    @property
    def est_bien_connu(self):
         return self.port < 1024

    def adresse(self):
        return f"{self.ip}:{self.port}"
    
    def __repr__(self):
            return f"Cible({self.ip}:{self.port})"
    
    def __eq__(self, autre):
        return self.ip == autre.ip and self.port == autre.port
    
c = Cible.depuis_texte("10.0.0.5:22")
print(c)
print(type(c.port))

print(Cible.port_valide(22)) 
print(Cible.port_valide(99999)) 

print(c.est_bien_connu)
d = Cible("10.0.0.5", 8080)
print(d.est_bien_connu)