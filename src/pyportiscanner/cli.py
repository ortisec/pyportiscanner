import argparse
import ipaddress
import socket
from pyportiscanner.scanner import scan_ports

def parse_ports(port_range: str) -> list[int]:
    try:
        start, end = map(int, port_range.split("-"))
        if not (1 <= start <= end <= 65535):
            raise ValueError
        return list(range(start, end + 1))
    except ValueError:
        raise argparse.ArgumentTypeError("El rango de puertos debe ser del tipo 1-1024")

def resolve_target(target: str) -> str:
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            raise argparse.ArgumentTypeError("IP o dominio inválido")

def main() -> None:
    parser = argparse.ArgumentParser(
    description="""PyPortiScanner - TCP Port Scanner básico en Python
    
    👤 Desarrollado por: ortisec
    🔗 GitHub: https://github.com/ortisec/pyportiscanner
    🌐 Website: https://ortisec.site/
            """.strip(),
    formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("target", type=resolve_target, help="IP o dominio objetivo")
    parser.add_argument(
        "--ports",
        required=True,
        type=parse_ports,
        help="Rango de puertos (ej: 1-1024)",
    )
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout por puerto")
    parser.add_argument("--workers", type=int, default=100, help="Hilos concurrentes")
    args = parser.parse_args()
    print(f"[+] Escaneando {args.target}...")
    open_ports = scan_ports(args.target, args.ports, args.timeout, args.workers)
    if open_ports:
        for port in open_ports:
            print(f"[+] {port} OPEN")
    else:
        print("[-] No se encontraron puertos abiertos")

if __name__ == "__main__":
    main()