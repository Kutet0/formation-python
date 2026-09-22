from core import Plugin

class PluginPing(Plugin):
    def __init__(self):
        super().__init__("ping")

    def run(self, cible):
        return f"ping {cible.adresse()}"