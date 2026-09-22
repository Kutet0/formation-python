from core import Plugin

class PluginBanniere(Plugin):
    def __init__(self):
        super().__init__("banniere")

    def run(self, cible):
        brut = b"SSH-2.0-OpenSSH_9.6\r\n"
        return brut.decode("utf-8", errors="replace").strip()