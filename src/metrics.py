from typing import List, Tuple
from src.scheduler import GanttEntry

class Metrics:
    """Cálculo de métricas de planificación."""
    @staticmethod
    def from_gantt(entries: List[GanttEntry]) -> dict:
        # TODO: calcular tiempos medios de respuesta, espera y retorno
        raise NotImplementedError