import json
import csv
from typing import List, Optional
from src.proceso import Proceso

class RepositorioProcesos:
    """Gestiona el conjunto de procesos con persistencia."""
    def __init__(self):
        self.procesos: List[Proceso] = []

    def agregar(self, proceso: Proceso):
        if self.obtener(proceso.pid):
            raise ValueError(f"PID '{proceso.pid}' ya existe en el repositorio.")
        self.procesos.append(proceso)

    def listar(self) -> List[Proceso]:
        return list(self.procesos)

    def eliminar(self, pid: str):
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def obtener(self, pid: str) -> Optional[Proceso]:
        return next((p for p in self.procesos if p.pid == pid), None)

    def guardar_json(self, ruta: str):
        with open(ruta, 'w') as f:
            json.dump([p.__dict__ for p in self.procesos], f)

    def cargar_json(self, ruta: str):
        with open(ruta) as f:
            datos = json.load(f)
        self._cargar_desde_dicts(datos)

    def guardar_csv(self, ruta: str):
        with open(ruta, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid','duracion','prioridad'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, ruta: str):
        with open(ruta) as f:
            reader = csv.DictReader(f, delimiter=';')
            datos = list(reader)
        dicts = [{ 'pid': d['pid'], 'duracion': int(d['duracion']), 'prioridad': int(d['prioridad']) } for d in datos]
        self._cargar_desde_dicts(dicts)

    def _cargar_desde_dicts(self, lista_dicts):
        from src.proceso import Proceso
        Proceso.resetear_registro()
        self.procesos.clear()
        for d in lista_dicts:
            self.procesos.append(Proceso(d['pid'], d['duracion'], d['prioridad']))