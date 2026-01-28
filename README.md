# 🔍 PyPortScanner

Una herramienta eficiente de **escaneo de puertos TCP** desarrollada en Python, diseñada para identificar puertos abiertos en hosts y dominios de forma rápida utilizando **multithreading**.

**👤 Desarrollado por:** [ortisec](https://ortisec.site/)  
**🔗 GitHub:** [ortisec/pyportscanner](https://github.com/ortisec/pyportiscanner)  
**🐋 Docker Hub:** [ortisec/pyportscanner](https://hub.docker.com/r/ortisec/pyportiscanner)

---

## Características

- ✅ **Escaneo TCP rápido** usando sockets
- ⚡ **Multithreading** para escaneo paralelo (hasta 100 hilos por defecto)
- 🎯 **Soporte para rangos de puertos personalizados** (ej: 1-1024)
- 🌐 **Resolución de dominios** automática (acepta IP o nombres de dominio)
- ⏱️ **Timeout configurable** por puerto
- 🐳 **Containerizado con Docker** para fácil despliegue
- 🔧 **Interfaz CLI intuitiva** con argparse
- 📦 **Instalable como herramienta de línea de comandos**

---

## 📦 Requisitos Previos

### Opción 1: Instalación Local
- **Python:** 3.14 o superior
- **Sistema operativo:** Windows, Linux, macOS
- **Permisos:** Acceso de red a los hosts objetivo

### Opción 2: Docker
- **Docker:** Versión 20.0 o superior

---

## 🚀 Instalación

### Instalación Local

1. **Clona el repositorio:**
```bash
git clone https://github.com/ortisec/pyportscanner.git
cd pyportscanner
```

2. **Instala el paquete:**
```bash
pip install -e .
```

Esto instalará la herramienta como comando `pps` disponible globalmente.

3. **Verifica la instalación:**
```bash
pps --help
```

### Usando Docker

1. **Construye la imagen:**
```bash
docker build -t pyportscanner .
```

2. **Ejecuta el escaneo:**
```bash
docker run pyportscanner <target> --ports 1-1024
```

---

## 💻 Uso

### Línea de Comandos

**Sintaxis básica:**
```bash
pps <target> --ports <rango>
```

#### Parámetros Requeridos:

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `target` | IP o dominio objetivo | `192.168.1.1` o `example.com` |
| `--ports` | Rango de puertos a escanear | `1-1024` |

#### Parámetros Opcionales:

| Parámetro | Descripción | Valor por defecto | Rango |
|-----------|-------------|-------------------|-------|
| `--timeout` | Tiempo de espera por puerto (segundos) | `1.0` | `0.1-10.0` |
| `--workers` | Número de hilos concurrentes | `100` | `1-1000` |

### Como Módulo Python

Puedes importar la función `scan_ports` en tus scripts:

```python
from pyportscanner.scanner import scan_ports

# Escanear puertos del 1 al 1024 en localhost
open_ports = scan_ports(
    host="127.0.0.1",
    ports=list(range(1, 1025)),
    timeout=1.0,
    workers=100
)

print(f"Puertos abiertos: {open_ports}")
```

---

## 🔄 Ejemplos

### Ejemplo 1: Escaneo Básico
Escanear los puertos comunes (1-1024) en un servidor:
```bash
pps 192.168.1.100 --ports 1-1024
```

**Salida esperada:**
```
[+] Escaneando 192.168.1.100...
[+] 22 OPEN
[+] 80 OPEN
[+] 443 OPEN
```

### Ejemplo 2: Escaneo con Dominio
Resolver y escanear un dominio:
```bash
pps example.com --ports 80-443
```

El programa resuelve automáticamente el dominio a su IP.

### Ejemplo 3: Escaneo Personalizado
Escanear con timeout mayor y menos hilos:
```bash
pps 10.0.0.5 --ports 1-65535 --timeout 2.0 --workers 50
```

### Ejemplo 4: Escaneo Rápido de Puertos Específicos
Escanear solo puertos web:
```bash
pps localhost --ports 80-80,443-443,8080-8080,3000-3000
```

### Ejemplo 5: Usar con Docker
```bash
docker run pyportscanner 192.168.1.1 --ports 1-1024
```

---

## ⚙️ Opciones Avanzadas

### Ajuste de Rendimiento

**Para redes lentas o con alto latency:**
```bash
pps target --ports 1-1024 --timeout 3.0 --workers 50
```

**Para escaneos rápidos de redes locales:**
```bash
pps target --ports 1-1024 --timeout 0.5 --workers 200
```

### Rango Máximo de Puertos
El rango válido de puertos es **1 a 65535**. Intentar un rango fuera de estos límites resultará en un error.

---

## 🏗️ Arquitectura

### Estructura del Proyecto
```
pyportscanner/
├── src/pyportscanner/
│   ├── __init__.py          # Inicializador del paquete
│   ├── scanner.py           # Lógica principal de escaneo
│   └── cli.py               # Interfaz de línea de comandos
├── Dockerfile               # Configuración para Docker
├── pyproject.toml           # Configuración del paquete
└── README.md                # Este archivo
```

### Componentes Principales

#### `scanner.py`
Módulo core que contiene la lógica de escaneo:

- **`scan_port(host, port, timeout)`**: Escanea un puerto individual
  - Retorna `True` si el puerto está abierto
  - Retorna `False` si está cerrado o no responde

- **`scan_ports(host, ports, timeout, workers)`**: Escanea múltiples puertos
  - Utiliza `ThreadPoolExecutor` para paralelismo
  - Retorna lista de puertos abiertos ordenada

#### `cli.py`
Interfaz de línea de comandos:

- **`parse_ports(port_range)`**: Valida y parsea el rango de puertos
- **`resolve_target(target)`**: Resuelve IP o dominio
- **`main()`**: Función principal que coordina el escaneo

### Flujo de Ejecución
```
1. Usuario ejecuta: pps <target> --ports <rango>
   ↓
2. CLI parsea argumentos y valida entradas
   ↓
3. Se resuelve el target (IP o dominio)
   ↓
4. Se valida el rango de puertos
   ↓
5. scanner.scan_ports() inicia el escaneo paralelo
   ↓
6. ThreadPoolExecutor crea hilos concurrentes
   ↓
7. Cada hilo escanea un puerto individual
   ↓
8. Resultados se recopilan y ordenan
   ↓
9. Se imprime salida con puertos abiertos
```

---

## ⚠️ Limitaciones y Consideraciones

### Requisitos Técnicos
- Requiere **Python 3.14+** (versión actual experimental)
- No tiene dependencias externas
- Compatible con sistemas POSIX y Windows

### Consideraciones de Seguridad
- **Uso legal:** Solo escanea hosts para los que tienes permiso
- **Firewall:** Algunos hosts pueden filtrar puertos con firewalls
- **Rate limiting:** Algunos ISP pueden detectar escaneos activos
- **Responsabilidad:** El usuario es responsable del uso de esta herramienta

### Limitaciones Conocidas
- **Escaneo SYN:** Usa escaneo TCP completo (no SYN half-open)
- **UDP:** Solo soporta puertos TCP, no UDP
- **Resolución DNS:** Requiere conectividad a servidores DNS
- **Timeout mínimo:** No se recomiendan timeouts menores a 0.1 segundos

### Casos de Uso
✅ Auditorías autorizadas de seguridad  
✅ Administración de servidores propios  
✅ Laboratorios de práctica  
❌ Escaneo de sistemas sin autorización (ILEGAL)

---

## 🔧 Solución de Problemas

### Problema: "ArgumentTypeError: El rango de puertos debe ser del tipo 1-1024"

**Causa:** Formato incorrecto del rango de puertos

**Solución:** Usa el formato `inicio-fin` (ej: `1-1024`)

### Problema: "ArgumentTypeError: IP o dominio inválido"

**Causa:** IP o dominio no válido o no resolvible

**Solución:** Verifica la IP o dominio, y asegúrate de tener conectividad

### Problema: Escaneo muy lento

**Causa:** Timeout muy alto o número de workers muy bajo

**Solución:** 
```bash
pps target --ports 1-1024 --timeout 0.5 --workers 200
```

### Problema: Resultados inconsistentes

**Causa:** Problemas de red o firewall intermitente

**Solución:** Aumenta el timeout y ejecuta nuevamente

---

## 📊 Rendimiento Esperado

**En red local (LAN):**
- Escaneo de 1000 puertos: ~5-10 segundos
- Escaneo de 65535 puertos: ~5-15 minutos

**En internet:**
- Variabilidad alta según la calidad de conexión
- Escaneo de 1000 puertos: ~30-60 segundos
- Recomendado usar timeout de 2-3 segundos

---

## 📝 Configuración en pyproject.toml

```toml
[project]
name = "pyportscanner"
version = "0.1.0"
description = "TCP Port Scanner básico en Python"
requires-python = ">=3.14"

[project.scripts]
pps = "pyportscanner.cli:main"
```

**Punto de entrada:** El comando `pps` ejecuta la función `main()` desde `cli.py`

---

## 🐳 Docker

### Crear Imagen
```bash
docker build -t pyportscanner:latest .
```

### Ejecutar Contenedor
```bash
docker run --rm pyportscanner 192.168.1.1 --ports 1-1024
```

### Especificar Opciones
```bash
docker run --rm pyportscanner target --ports 1-65535 --timeout 2.0 --workers 50
```

---

## 📜 Licencia

Este proyecto es de **código abierto**. Consulta con el autor para detalles de licencia específicos.

**Autor:** ortisec  
**Repositorio:** https://github.com/ortisec/pyportscanner  
**Sitio Web:** https://ortisec.site/

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commitea tus cambios
4. Push a la rama
5. Abre un Pull Request

---

## ❓ Preguntas y Soporte

Para reportar bugs, sugerencias o preguntas:
- Abre un issue en [GitHub Issues](https://github.com/ortisec/pyportscanner/issues)
- Contacta al autor en https://ortisec.site/

---

**Última actualización:** 26 de enero de 2026  
**Versión del Proyecto:** 0.1.0
