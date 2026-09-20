def construire_commande(cible, *ports, timeout=2, verbose=False, **options):
    partie = [f"scan {cible}"]

    if ports:
        port = [str(p) for p in ports]
        port_str = ",".join(port)
        partie.append(f"--ports {port_str}")
    
    partie.append(f"--timeout {timeout}")

    if verbose:
        partie.append("--verbose")
    
    if options:
        for key, value in options.items():
            partie.append(f"--{key} {value}")

    commande = " ".join(partie)
    return commande

commande = construire_commande("10.0.0.5")
print(commande)
commande = construire_commande("10.0.0.5", 22, 80, 443, timeout=5, verbose=True)
print(commande)
commande = construire_commande("10.0.0.5", 22, retry=3, proxy="off")
print(commande)