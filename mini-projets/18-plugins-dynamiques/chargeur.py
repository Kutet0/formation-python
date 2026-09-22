import pkgutil, plugins, inspect, importlib
from core import Plugin, Cible

def charger_plugins():
    trouves = []
    for info in pkgutil.iter_modules(plugins.__path__):
        module = importlib.import_module(f"plugins.{info.name}")
        for nom, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, Plugin) and obj is not Plugin:
                trouves.append(obj())
    return trouves

c = Cible("10.0.0.5", 22)
for p in charger_plugins():
    print(p.nom, "->", p.run(c))