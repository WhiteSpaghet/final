import pytest
from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler

@pytest.fixture(autouse=True)
def reset_pids():
    Proceso.resetear_registro()

def test_fcfs_planificacion():
    p1 = Proceso('P1', 3, 1)
    p2 = Proceso('P2', 2, 2)
    gantt = FCFSScheduler().planificar([p1, p2])
    assert gantt == [('P1',0,3),('P2',3,5)]

def test_rr_planificacion():
    p1 = Proceso('P1', 4, 1)
    p2 = Proceso('P2', 3, 1)
    gantt = RoundRobinScheduler(2).planificar([p1,p2])
    assert gantt == [('P1',0,2),('P2',2,4),('P1',4,6),('P2',6,7)]