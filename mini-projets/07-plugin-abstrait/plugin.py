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

class PluginPing(Plugin):
    def run(self, cible):
        return f"ping {cible.adresse()}"

class PluginScan(Plugin):
    def run(self, cible):
        return f"scan {cible.adresse()}"
    
class PluginBanniere(Plugin):
    def run(self, cible):
        brut = b"SSH-2.0-OpenSSH_9.6\r\n"
        return brut.decode("utf-8", errors="replace").strip()
    
cible = Cible("10.0.0.5", 22)

ping = PluginPing("ping")
print(ping.decrire())
print(ping.run(cible))

plugins = [PluginPing("ping"), PluginScan("scan"), PluginBanniere("banniere")]
for p in plugins:
    print(p.run(cible))