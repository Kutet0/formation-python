def decoder_banniere(brut):
    texte = brut.decode("utf_8", errors="replace").strip()
    return texte

def encoder_requete(texte):
    brut = texte.encode("utf-8")
    return brut

print(decoder_banniere(b"SSH-2.0-OpenSSH_9.6\r\n"))
print(decoder_banniere(b"HTTP/1.1 200 OK\r\n"))
print(decoder_banniere(b"\xe9 serveur bizarre"))
r = encoder_requete("GET / HTTP/1.0")
print(r)
print(type(r))