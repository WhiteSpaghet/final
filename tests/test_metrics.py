import pytest
from src.scheduler import GanttEntry
from src.metrics import Metrics

@pytest.mark.parametrize('entries, expected', [
    ([('P1',0,3),('P2',3,5)], {'tiempo_respuesta_medio':0.0,'tiempo_retorno_medio':4.0,'tiempo_espera_medio':2.0}),
])
def test_metrics(entries, expected):
    result = Metrics.from_gantt(entries)
    assert result == expected