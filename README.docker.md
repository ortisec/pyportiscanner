# PyPortiScanner — Uso con Docker

Guía rápida y completa para ejecutar PyPortiScanner exclusivamente con Docker, sin instalación local de Python.

---

## Requisitos
- Docker 20+ instalado y funcionando
- Conectividad de red hacia el objetivo

---

## Descargar la imagen publicada

```bash
docker pull ortisec/pyportiscanner:latest
```

También puedes ejecutar directamente (Docker descargará la imagen si no existe):

```bash
docker run --rm ortisec/pyportiscanner:latest --help
```

---

## Ejecución básica
- Sintaxis:

```bash
docker run --rm ortisec/pyportiscanner:latest <target> --ports <rango>
```

- Ejemplo:

```bash
docker run --rm ortisec/pyportiscanner:latest 192.168.1.10 --ports 1-1024
```

---

## Parámetros disponibles
- `target`: IP o dominio objetivo
- `--ports`: rango de puertos (ej. `1-1024`)
- `--timeout`: segundos por puerto (por defecto `1.0`)
- `--workers`: hilos concurrentes (por defecto `100`)

Ejemplo completo:

```bash
docker run --rm ortisec/pyportiscanner:latest 10.0.0.5 --ports 1-65535 --timeout 2.0 --workers 50
```

---

## Notas de red y plataforma
- Linux:
  - Para escanear puertos del propio host desde el contenedor, usa red de host:

    ```bash
    docker run --rm --network host ortisec/pyportiscanner:latest localhost --ports 1-1024
    ```

- Windows y macOS (Docker Desktop):
  - `--network host` no está disponible como en Linux.
  - Para alcanzar servicios del host, utiliza el nombre `host.docker.internal`:

    ```bash
    docker run --rm ortisec/pyportiscanner:latest host.docker.internal --ports 1-1024
    ```

- Políticas/FW:
  - Firewalls y políticas corporativas pueden bloquear o limitar escaneos.
  - Usa timeouts y workers adecuados según la red.

---

## Ejemplos rápidos
- Escaneo básico LAN:

```bash
docker run --rm ortisec/pyportiscanner:latest 192.168.1.100 --ports 1-1024
```

- Escaneo rápido de puertos web:

```bash
docker run --rm ortisec/pyportiscanner:latest example.com --ports 80-80,443-443,8080-8080,3000-3000
```

- Ajuste para redes lentas:

```bash
docker run --rm ortisec/pyportiscanner:latest target --ports 1-1024 --timeout 3.0 --workers 50
```

---

## Solución de problemas
- Argumento inválido de puertos:
  - Formato esperado: `inicio-fin` (ej. `1-1024`)
- IP/Dominio inválido:
  - Verifica conectividad DNS y formato del objetivo
- Escaneo lento o inconsistente:
  - Aumenta `--timeout` o ajusta `--workers`
