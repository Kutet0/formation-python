import asyncio, time

async def port_ouvert_async(ip, port, timeout=1):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return False

async def scan_async(ip, ports, timeout=1):
    tache = [port_ouvert_async(ip, p, timeout) for p in ports]
    resultat = await asyncio.gather(*tache)
    return [p for p, ouvert in zip(ports, resultat) if ouvert]

ports = list(range(8000, 8101))
ouverts = asyncio.run(scan_async("127.0.0.1", ports))
print(ouverts) 

debut = time.time()
tout = asyncio.run(scan_async("127.0.0.1", list(range(1, 1001))))
print(f"{tout} en {time.time()-debut:.2f}s")