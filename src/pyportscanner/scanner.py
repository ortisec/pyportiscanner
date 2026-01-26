import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host: str, port: int, timeout: float) -> bool:
    """
    Devuelve True si el puerto está abierto, False en caso contrario.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0


def scan_ports(
    host: str,
    ports: list[int],
    timeout: float = 1.0,
    workers: int = 100,
) -> list[int]:
    """
    Escanea una lista de puertos y devuelve los que están abiertos.
    """
    open_ports = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(scan_port, host, port, timeout): port
            for port in ports
        }

        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)

    return sorted(open_ports)
