import os
import pytest
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos

@pytest.fixture(autouse=True)

def reset_pids():
    Proceso.resetear_registro()

@pytest.fixture
def tmp_file(tmp_path):
    return tmp_path / "procs"


def test_agregar_y_listar():
    repo = RepositorioProcesos()
    p = Proceso('P1',1,1)
    repo.agregar(p)
    assert repo.listar() == [p]


def test_persistencia_json(tmp_file):
    repo = RepositorioProcesos()
    repo.agregar(Proceso('P1',1,1))
    path = str(tmp_file) + '.json'
    repo.guardar_json(path)
    repo2 = RepositorioProcesos()
    repo2.cargar_json(path)
    assert len(repo2.listar()) == 1


def test_persistencia_csv(tmp_file):
    repo = RepositorioProcesos()
    repo.agregar(Proceso('P1',2,2))
    path = str(tmp_file) + '.csv'
    repo.guardar_csv(path)
    repo2 = RepositorioProcesos()
    repo2.cargar_csv(path)
    assert len(repo2.listar()) == 1