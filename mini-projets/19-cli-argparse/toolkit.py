import argparse

def parse_plage(port_str):
    debut, fin = port_str.strip().split("-")
    return int(debut), int(fin)

def parse_args():
    args = [args.cible]
    print(args)

parser = argparse.ArgumentParser(description="Scanner de ports")
parser.add_argument("cible", help="l'IP à scanner")
parser.add_argument("--ports", default="1-100", help="plage, ex: 1-1000")
parser.add_argument("--timeout", type=float, default=1.0)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

commande = []

debut, fin = parse_plage(args.ports)
parse_args(args)