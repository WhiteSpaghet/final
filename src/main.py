import argparse
from src.repositorio import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.metrics import Metrics

def main():
    parser = argparse.ArgumentParser(description='Simulador de planificación de CPU')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--add', nargs=3, metavar=('PID','DURACION','PRIORIDAD'), help='Agregar un proceso')
    group.add_argument('--list', action='store_true', help='Listar procesos registrados')
    group.add_argument('--run', action='store_true', help='Ejecutar planificación')

    parser.add_argument('--algoritmo', choices=['FCFS','RR'], default='FCFS', help='Algoritmo de planificación')
    parser.add_argument('--quantum', type=int, default=1, help='Quantum para Round-Robin')
    parser.add_argument('--input', help='Archivo JSON/CSV con procesos')
    parser.add_argument('--output', help='Guardar resultados')
    args = parser.parse_args()

    repo = RepositorioProcesos()
    # Cargar persistencia si se provee input
    if args.input:
        if args.input.endswith('.json'):
            repo.cargar_json(args.input)
        else:
            repo.cargar_csv(args.input)

    if args.add:
        pid, duracion, prioridad = args.add
        try:
            p = Proceso(pid, int(duracion), int(prioridad))
            repo.agregar(p)
            print(f"Proceso agregado: {pid}, duracion={duracion}, prioridad={prioridad}")
        except ValueError as e:
            print(f"Error al agregar proceso: {e}")
            return 1
        # Guardar cambios si output
        if args.output:
            if args.output.endswith('.json'):
                repo.guardar_json(args.output)
            else:
                repo.guardar_csv(args.output)
        return 0

    if args.list:
        procesos = repo.listar()
        if not procesos:
            print("No hay procesos registrados.")
        else:
            print("Listado de procesos:")
            for p in procesos:
                print(f"PID={p.pid}, duracion={p.duracion}, prioridad={p.prioridad}")
        return 0

    if args.run:
        procesos = repo.listar()
        if not procesos:
            print("No hay procesos cargados. Use --add o --input para especificar procesos.")
            return 1
        scheduler = FCFSScheduler() if args.algoritmo == 'FCFS' else RoundRobinScheduler(args.quantum)
        gantt = scheduler.planificar(procesos)
        metrics = Metrics.from_gantt(gantt)
        print('Diagrama de Gantt:', gantt)
        print('Métricas medias:', metrics)
        if args.output:
            # Serializar resultados según extensión si se desea
            pass
        return 0

    return 0