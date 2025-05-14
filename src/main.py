import argparse
from src.repositorio import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.metrics import Metrics

def main():
    parser = argparse.ArgumentParser(description='Simulador de planificación de CPU')
    parser.add_argument('--algoritmo', choices=['FCFS','RR'], required=True, help='Algoritmo de planificación')
    parser.add_argument('--quantum', type=int, default=1, help='Quantum para Round-Robin')
    parser.add_argument('--input', help='Archivo JSON/CSV con procesos')
    parser.add_argument('--output', help='Guardar resultados')
    args = parser.parse_args()

    repo = RepositorioProcesos()
    if args.input:
        if args.input.endswith('.json'):
            repo.cargar_json(args.input)
        else:
            repo.cargar_csv(args.input)

    procesos = repo.listar()
    scheduler = FCFSScheduler() if args.algoritmo == 'FCFS' else RoundRobinScheduler(args.quantum)

    gantt = scheduler.planificar(procesos)
    metrics = Metrics.from_gantt(gantt)
    print('Diagrama de Gantt:', gantt)
    print('Métricas medias:', metrics)

    if args.output:
        # Serializar resultados según extensión
        pass

    return 0