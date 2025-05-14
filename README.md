https://github.com/WhiteSpaghet/final.git
# Proyecto Scheduler

Este proyecto es un planificador de procesos que implementa diferentes algoritmos de planificación. Es ideal para aprender y experimentar con conceptos de sistemas operativos relacionados con la gestión de procesos.

## Estructura del Proyecto

- `main.py`: Archivo principal que actúa como punto de entrada del programa.
- `launcher.py`: Contiene la función `launch()` para inicializar el programa.
- `src/`: Carpeta que contiene la lógica principal del programa.
- `tests/`: Carpeta con pruebas unitarias implementadas con `pytest`.

## Instalación

Sigue los pasos a continuación para configurar el entorno y ejecutar el programa:

1. Crea un entorno virtual:
    ```bash
    python3 -m venv venv
    ```

2. Activa el entorno virtual:
    - En Linux/MacOS:
      ```bash
      source venv/bin/activate
      ```
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

El programa se ejecuta desde la línea de comandos. A continuación, se muestra un ejemplo de uso:

```bash
./main.py --input procesos.json --algoritmo RR --quantum 2
```

### Parámetros

- `--input`: Archivo JSON que contiene la lista de procesos a planificar.
- `--algoritmo`: Algoritmo de planificación a utilizar. Los valores posibles son:
  - `FCFS` (First-Come, First-Served)
  - `SJF` (Shortest Job First)
  - `RR` (Round Robin)
- `--quantum`: (Opcional) Valor del quantum para el algoritmo Round Robin.

### Ejemplo de Archivo JSON

El archivo `procesos.json` debe tener el siguiente formato:

```json
[
  {"id": 1, "llegada": 0, "duracion": 5},
  {"id": 2, "llegada": 2, "duracion": 3},
  {"id": 3, "llegada": 4, "duracion": 1}
]
```

## Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
pytest
```

Esto ejecutará todas las pruebas en la carpeta `tests/` y mostrará los resultados.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección de errores:
    ```bash


