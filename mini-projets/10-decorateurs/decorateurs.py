
def chrono(func):
    def wrapper(*args, **kwargs):
        import time
        debut = time.time()
        resultat = func(*args, **kwargs)
        duree = time.time() - debut
        print(f"{func.__name__} a pris {duree:.3f}s")
        return resultat
    return wrapper

def log(func):
    def wrapper(*args, **kwargs):
        arguments = [str(arg) for arg in args]
        args_str = ",".join(arguments)
        kwarguments = []
        for key, value in kwargs.items():
            kwarguments.append(f"{key}: {value}")
        print(f"appel de {func.__name__} avec args=({args_str}) kwargs={kwarguments}")
        resultat = func(*args, **kwargs)
        print(f"{func.__name__} a renvoyé {resultat}")
        return resultat
    return wrapper

@chrono
def addition(a, b):
    return a + b

print(addition(2, 3))

@log
def scanner(cible, timeout=2, verbose=False):
    return f"scan de {cible}"

scanner("10.0.0.5", timeout=5)