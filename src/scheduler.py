from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso

GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    """Interfaz general de un planificador de CPU."""

    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        # TODO: implementar FCFS
        raise NotImplementedError

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        # TODO: implementar Round-Robin
        raise NotImplementedError