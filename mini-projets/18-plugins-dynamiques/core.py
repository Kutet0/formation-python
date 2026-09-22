from abc import ABC, abstractmethod


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

class Plugin(ABC):
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def run(self, cible):
        ...
    
    def decrire(self):
        return f"Plugin: {self.nom}"