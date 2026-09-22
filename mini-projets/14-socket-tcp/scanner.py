import socket

def port_ouvert(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        code = s.connect_ex((ip, port))
        if code == 0:
            return True
        else:
            return False

def plage_ports(debut, fin):
    port = debut
    while port <= fin:
        yield port
        port += 1

print(port_ouvert("127.0.0.1", 8080))
print(port_ouvert("127.0.0.1", 9999))

for p in plage_ports(8078, 8082):
    if port_ouvert("127.0.0.1", p):
        print(f"port {p} ouvert")
