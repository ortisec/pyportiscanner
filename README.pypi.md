<p align="center">
  <img src="https://raw.githubusercontent.com/ortisec/pyportiscanner/e097fa149a5b1741b8630e09c2177bf3af346bea/src/assets/pyportiscanner-logo.svg"
       width="12.5%"
       alt="Logo PyPortiScanner">
</p>


# PyPortiScanner

**PyPortiScanner** es una herramienta eficiente y robusta para el escaneo de puertos TCP, diseñada para identificar servicios abiertos en hosts y dominios mediante el uso de sockets y concurrencia. Su arquitectura permite realizar auditorías de red rápidas y precisas, facilitando tanto el uso interactivo desde la línea de comandos como su integración programática en proyectos de Python.

---

## 📋 Características Principales

*   **Escaneo TCP Multihilo**: Ejecución paralela optimizada para reducir tiempos de espera en rangos amplios de puertos.
*   **Resolución de Nombres**: Capacidad para resolver automáticamente dominios a direcciones IP.
*   **Flexibilidad**: Configuración granular de *timeouts* y número de hilos de ejecución (*workers*).
*   **Doble Modalidad**: Funciona como herramienta de línea de comandos (CLI) y como librería importable.

## 🚀 Instalación

Para instalar la última versión estable desde PyPI, ejecute el siguiente comando en su terminal:

```bash
pip install pyportiscanner
```

*Nota: Se requiere Python 3.10 o superior.*

## 💻 Uso Básico

### Interfaz de Línea de Comandos (CLI)

Una vez instalado, el comando `pps` estará disponible en su sistema.

**Sintaxis general:**
```bash
pps <objetivo> --ports <rango> [opciones]
```

**Ejemplo de uso rápido:**
Escanear los puertos del 1 al 1024 en un host específico:

```bash
pps 192.168.1.10 --ports 1-1024
```

**Opciones comunes:**
*   `--timeout <segundos>`: Define el tiempo máximo de espera por puerto (por defecto: 1.0).
*   `--workers <número>`: Establece la cantidad de hilos concurrentes (por defecto: 100).

### Integración en Python

PyPortiScanner puede importarse como un módulo para integrar la funcionalidad de escaneo en sus propios scripts o aplicaciones.

**Ejemplo de implementación:**

```python
from pyportiscanner.scanner import scan_ports

# Definir parámetros de escaneo
host_objetivo = "scanme.nmap.org"
rango_puertos = list(range(20, 100))  # Puertos del 20 al 99

# Ejecutar el escaneo
puertos_abiertos = scan_ports(
    host=host_objetivo,
    ports=rango_puertos,
    timeout=2.0,
    workers=50
)

print(f"Puertos abiertos detectados: {puertos_abiertos}")
```

## 📄 Licencia

Este proyecto se distribuye bajo licencia de código abierto. Para más detalles sobre los términos de uso y distribución, por favor consulte el repositorio oficial.

---
**Desarrollado por ortisec**  
[Repositorio Oficial](https://github.com/ortisec/pyportiscanner) | [Sitio Web](https://ortisec.site/)
