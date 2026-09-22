from core import Plugin

class PluginScan(Plugin):
    def __init__(self):
        super().__init__("scan")

    def run(self, cible):
        return f"scan {cible.adresse()}"