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
    
a = Cible("10.0.0.5", "22") # note : port passé en str
print(a) # -> Cible(10.0.0.5:22)
print(a.adresse()) # -> 10.0.0.5:22
print(a.port, type(a.port)) # -> 22 (bien converti !)
b = Cible("10.0.0.5", 22)
print(a == b) # -> True
c = Cible("10.0.0.5", 80)
print(a == c) # -> False
cibles = [a, b, c]