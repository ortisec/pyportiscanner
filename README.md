<p align="center">
  <img src="https://raw.githubusercontent.com/ortisec/pyportiscanner/e097fa149a5b1741b8630e09c2177bf3af346bea/src/assets/pyportiscanner-logo.svg"
       width="25%"
       alt="Logo PyPortiScanner">
</p>



# PyPortiScanner

PyPortiScanner es una herramienta de escaneo de puertos TCP escrita en Python, enfocada en velocidad y simplicidad. Ofrece una CLI práctica y una API de fácil integración para detectar puertos abiertos en hosts o dominios mediante ejecución concurrente.

---

## Características

- Escaneo TCP concurrente (multithreading)
- Resolución automática de dominios
- Configuración de timeout y número de workers
- Uso como CLI y como librería de Python

---

## Instalación

```bash
pip install pyportiscanner
```

Requisitos: Python 3.14 o superior.

Instalación desde código fuente (desarrollo):
```bash
git clone https://github.com/ortisec/pyportiscanner.git
cd pyportiscanner
pip install -e .
```

Docker:
```bash
docker build -t pyportiscanner .
```

---

## Uso Rápido (CLI)

```bash
pps <objetivo> --ports <rango> [opciones]
```

Ejemplo:
```bash
pps 192.168.1.10 --ports 1-1024
```

Opciones comunes:
- `--timeout <segundos>` (por defecto: 1.0)
- `--workers <número>` (por defecto: 100)

---

## Parámetros y opciones

- Requeridos:
  - `target`: IP o dominio objetivo (ej. `192.168.1.10` o `example.com`)
  - `--ports`: Rango de puertos a escanear (formato `inicio-fin`, ej. `1-1024`)
- Opcionales:
  - `--timeout`: Tiempo de espera por puerto (segundos). Rango recomendado: `0.1–10.0`
  - `--workers`: Número de hilos concurrentes. Rango recomendado: `1–1000`

Salida típica:
```
[+] Escaneando 192.168.1.10...
[+] 22 OPEN
[+] 80 OPEN
[+] 443 OPEN
```

---

## API de Python

```python
from pyportiscanner.scanner import scan_ports

puertos = scan_ports(
    host="scanme.nmap.org",
    ports=list(range(20, 100)),
    timeout=2.0,
    workers=50
)

print(puertos)
```

---

## Ejemplos

- Escaneo básico:
```bash
pps 192.168.1.100 --ports 1-1024
```

- Escaneo de dominio:
```bash
pps example.com --ports 80-443
```

- Escaneo completo con ajustes:
```bash
pps 10.0.0.5 --ports 1-65535 --timeout 2.0 --workers 50
```

- Puertos específicos (rango individual por puerto):
```bash
pps localhost --ports 80-80,443-443,8080-8080,3000-3000
```

---

## Docker

Construcción y ejecución:
```bash
docker build -t pyportiscanner .
docker run --rm pyportiscanner 192.168.1.1 --ports 1-1024
```

---

## Opciones avanzadas y rendimiento

- Redes lentas o alta latencia:
```bash
pps target --ports 1-1024 --timeout 3.0 --workers 50
```

- Redes locales rápidas:
```bash
pps target --ports 1-1024 --timeout 0.5 --workers 200
```

- Rango válido de puertos: `1–65535`

Rendimiento esperado:
- LAN: 1000 puertos ~ 5–10 s; 65535 puertos ~ 5–15 min
- Internet: 1000 puertos ~ 30–60 s (variable)

---

## Arquitectura del proyecto

```
pyportiscanner/
├── src/pyportiscanner/
│   ├── __init__.py          # Inicializador del paquete
│   ├── scanner.py           # Lógica principal de escaneo
│   └── cli.py               # Interfaz de línea de comandos
├── Dockerfile               # Configuración para Docker
├── pyproject.toml           # Configuración del paquete
└── README.md                # Este archivo
```

Componentes principales:
- `scanner.py`
  - `scan_port(host, port, timeout)` → True si abierto, False si cerrado
  - `scan_ports(host, ports, timeout, workers)` → lista de puertos abiertos ordenada
- `cli.py`
  - `parse_ports(port_range)` → validación y parseo de rangos
  - `resolve_target(target)` → resolución de IP/dominio
  - `main()` → coordinación del flujo de ejecución

---

## Seguridad y consideraciones

- Escanea únicamente sistemas para los que tengas autorización.
- Los resultados pueden variar por firewalls y condiciones de red.
- El uso indebido puede ser ilegal; el usuario es responsable de su aplicación.

---

## Solución de problemas

- Error de formato del rango de puertos:
  - Mensaje: `ArgumentTypeError: El rango de puertos debe ser del tipo 1-1024`
  - Solución: usa `inicio-fin` (ej. `1-1024`)
- IP o dominio inválido:
  - Mensaje: `ArgumentTypeError: IP o dominio inválido`
  - Solución: verifica conectividad y formato
- Escaneo lento:
  - Causa: timeout alto o pocos workers
  - Solución:
```bash
pps target --ports 1-1024 --timeout 0.5 --workers 200
```
- Resultados inconsistentes:
  - Causa: red inestable o firewall
  - Solución: aumenta timeout y reintenta

---

## Enlaces

- GitHub: https://github.com/ortisec/pyportiscanner
- Docker Hub: https://hub.docker.com/r/ortisec/pyportiscanner
- Autor: https://ortisec.site/

---

## Licencia

Proyecto de código abierto. Consulte el repositorio para más detalles.

---

## Contribuir

Las contribuciones son bienvenidas:
1. Realiza un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección.
3. Realiza commits atómicos y descriptivos.
4. Envía tus cambios mediante un Pull Request.
5. Asegura que tu PR incluya pruebas y documentación cuando aplique.
