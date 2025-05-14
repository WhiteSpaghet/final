from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso

GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    """Interfaz general de un planificador de CPU."""
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Simula la planificación y devuelve un diagrama de Gantt."""
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        # FCFS: ejecutar en orden de llegada
        gantt: List[GanttEntry] = []
        tiempo_actual = 0
        for p in procesos:
            p.tiempo_inicio = tiempo_actual
            p.tiempo_fin = tiempo_actual + p.duracion
            gantt.append((p.pid, p.tiempo_inicio, p.tiempo_fin))
            tiempo_actual = p.tiempo_fin
        return gantt

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        # Round-Robin: ciclos con quantum
        gantt: List[GanttEntry] = []
        tiempo = 0
        cola = procesos.copy()
        for p in cola:
            p.tiempo_restante = p.duracion
            p.tiempo_inicio = None
            p.tiempo_fin = None
        while cola:
            p = cola.pop(0)
            if p.tiempo_inicio is None:
                p.tiempo_inicio = tiempo
            ejecucion = min(self.quantum, p.tiempo_restante)
            inicio = tiempo
            fin = tiempo + ejecucion
            gantt.append((p.pid, inicio, fin))
            tiempo += ejecucion
            p.tiempo_restante -= ejecucion
            if p.tiempo_restante > 0:
                cola.append(p)
            else:
                p.tiempo_fin = tiempo
        return gantt