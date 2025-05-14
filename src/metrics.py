from typing import List, Dict
from src.scheduler import GanttEntry

class Metrics:
    """Cálculo de métricas de planificación."""
    @staticmethod
    def from_gantt(entries: List[GanttEntry]) -> Dict[str, float]:
        tiempos_inicio = {}
        tiempos_fin = {}
        for pid, inicio, fin in entries:
            if pid not in tiempos_inicio:
                tiempos_inicio[pid] = inicio
            tiempos_fin[pid] = fin
        n = len(tiempos_inicio)
        total_resp = total_retorno = total_espera = 0
        for pid in tiempos_inicio:
            t_llegada = 0
            t_inicio = tiempos_inicio[pid]
            t_fin = tiempos_fin[pid]
            duracion = next(fin - ini for p, ini, fin in entries if p == pid)
            t_resp = t_inicio - t_llegada
            t_retorno = t_fin - t_llegada
            t_espera = t_retorno - duracion
            total_resp += t_resp
            total_retorno += t_retorno
            total_espera += t_espera
        return {
            'tiempo_respuesta_medio': total_resp / n if n else 0,
            'tiempo_retorno_medio': total_retorno / n if n else 0,
            'tiempo_espera_medio': total_espera / n if n else 0,
        }