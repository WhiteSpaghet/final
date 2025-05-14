# final
https://github.com/WhiteSpaghet/final.git
# proyecto-scheduler

## Estructura
- `main.py`: punto de entrada.
- `launcher.py`: define la función launch().
- `src/`: paquete principal con la lógica.
- `tests/`: pruebas unitarias con pytest.

## Instalación\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


USO
./main.py --algoritmo FCFS --input procesos.json

TESTS
pytest