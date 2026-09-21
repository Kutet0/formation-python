class CibleInvalide(Exception):
    pass

def parser_cible(ligne):
    morceaux = ligne.strip().split(":")
    if len(morceaux) != 2:
        raise CibleInvalide("Séparateur manquant.")        
    ip, port = morceaux
    try:
        port = int(port)
    except ValueError:
        raise CibleInvalide("Le port n'est pas un nombre.")        
    return {"ip": ip, "port": port}

def parser_toute(lignes):
    valides = [] 
    rejetees = 0
    try:
        for ligne in lignes:
            try:
                cible = parser_cible(ligne)
                valides.append(cible)
            except CibleInvalide as error:
                print(f"ligne rejetée : {error}")
                rejetees += 1
    finally:
        print(f"{len(valides)} valide, {rejetees} rejeté")
    return valides                     

lignes = ["192.168.1.10:22", "machin", "10.0.0.5:abc", "10.0.0.5:443"]

valide = parser_toute(lignes)
