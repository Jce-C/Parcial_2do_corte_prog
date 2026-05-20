# DOCUMENTACION — Parcial Jose Carlos

## Descripcion general

Programa que toma cada letra del nombre "Jose Carlos", asigna un pais que empiece con esa letra, consulta la API de `restcountries.com` en paralelo usando `ThreadPoolExecutor`, y muestra los resultados en una tabla alineada con metricas de tiempo.

---

## Regla de letras

| Letra | Pais    | Nota                          |
|-------|---------|-------------------------------|
| J     | Japan   |                               |
| o     | Oman    |                               |
| s     | Spain   |                               |
| e     | Ecuador |                               |
| C     | Canada  |                               |
| a     | Argentina |                             |
| r     | Romania |                               |
| l     | Laos    |                               |
| o     | (omitida) | No hay otro pais con O     |
| s     | Sudan   | Pais distinto con la misma letra |

---

## Archivos

| Archivo          | Rol                                      |
|------------------|------------------------------------------|
| `main.py`        | Punto de entrada, define los datos y orquesta la ejecucion |
| `modelos.py`     | Clase `Country` — modelo de datos        |
| `api.py`         | Clase `CountryAPI` — logica HTTP y concurrencia |
| `tabla.py`       | Funciones de visualizacion (tabla + metricas) |
| `requirements.txt` | Dependencias del proyecto              |

---