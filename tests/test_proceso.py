import pytest
from src.proceso import Proceso


def test_crear_proceso_valido():
    p = Proceso('P1', 5, 1)
    assert p.pid == 'P1'
    assert p.duracion == 5
    assert p.prioridad == 1

@pytest.mark.parametrize('pid', ['', 'P1'] )
def test_pid_unico(pid):
    Proceso.resetear_registro()
    if pid == '':
        with pytest.raises(ValueError): Proceso(pid, 3, 1)
    else:
        Proceso(pid, 3, 1)
        with pytest.raises(ValueError): Proceso(pid, 4, 2)