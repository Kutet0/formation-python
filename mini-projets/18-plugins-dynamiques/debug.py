import plugins, pkgutil, importlib, inspect
from core import Plugin

for info in pkgutil.iter_modules(plugins.__path__):
    module = importlib.import_module(f"plugins.{info.name}")
    print(f"\n[{info.name}] classes trouvées :")
    for nom, obj in inspect.getmembers(module, inspect.isclass):
        garde = issubclass(obj, Plugin) and obj is not Plugin
        print(f"   {nom:20} issubclass(Plugin)={issubclass(obj, Plugin)}  gardé={garde}")