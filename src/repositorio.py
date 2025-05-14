import json
import csv
from typing import List, Optional
from src.proceso import Proceso

class RepositorioProcesos:
    """Gestiona el conjunto de procesos, con operaciones CRUD y persistencia."""
    def __init__(self):
        # Lista interna de procesos
        self.procesos: List[Proceso] = []

    def agregar(self, proceso: Proceso):
        """Agrega un proceso, verificando unicidad de PID."""
        if self.obtener(proceso.pid):
            raise ValueError(f"PID '{proceso.pid}' ya existe en el repositorio.")
        self.procesos.append(proceso)

    def listar(self) -> List[Proceso]:
        """Devuelve todos los procesos registrados."""
        return list(self.procesos)

    def eliminar(self, pid: str):
        """Elimina un proceso por su PID."""
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def obtener(self, pid: str) -> Optional[Proceso]:
        """Obtiene un proceso dado su PID, o None si no existe."""
        return next((p for p in self.procesos if p.pid == pid), None)

    # Persistencia en JSON
    def guardar_json(self, ruta: str):
        """Guarda la lista de procesos en formato JSON."""
        with open(ruta, 'w') as f:
            data = [
                {'pid': p.pid, 'duracion': p.duracion, 'prioridad': p.prioridad}
                for p in self.procesos
            ]
            json.dump(data, f, indent=2)

    def cargar_json(self, ruta: str):
        """Carga procesos desde un archivo JSON, reemplazando los existentes."""
        with open(ruta) as f:
            datos = json.load(f)
        self._cargar_desde_dicts(datos)

    # Persistencia en CSV
    def guardar_csv(self, ruta: str):
        """Guarda la lista de procesos en formato CSV (delimitador ';')."""
        with open(ruta, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, ruta: str):
        """Carga procesos desde un archivo CSV (delimitador ';'), reemplazando los existentes."""
        with open(ruta) as f:
            reader = csv.DictReader(f, delimiter=';')
            datos = [
                {'pid': row['pid'], 'duracion': int(row['duracion']), 'prioridad': int(row['prioridad'])}
                for row in reader
            ]
        self._cargar_desde_dicts(datos)

    def _cargar_desde_dicts(self, lista_dicts: List[dict]):
        """Helper: crea procesos a partir de dicts y reemplaza la lista interna."""
        from src.proceso import Proceso
        # Resetear registro de PIDs para evitar duplicados
        Proceso.resetear_registro()
        self.procesos.clear()
        for d in lista_dicts:
            p = Proceso(d['pid'], d['duracion'], d['prioridad'])
            self.procesos.append(p)
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