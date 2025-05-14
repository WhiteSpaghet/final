import sys
from src.repositorio import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.metrics import Metrics
from src.proceso import Proceso


def main():
    repo = RepositorioProcesos()
    print("Simulador de planificación de CPU")

    while True:
        print("Menú:")
        print("1. Agregar proceso")
        print("2. Listar procesos")
        print("3. Cargar procesos desde archivo")
        print("4. Guardar procesos a archivo")
        print("5. Ejecutar planificación")
        print("6. Salir")
        opcion = input("Selecciona una opción [1-6]: ").strip()

        if opcion == '1':
            pid = input("PID: ").strip()
            dur = input("Duración (int): ").strip()
            pri = input("Prioridad (int): ").strip()
            try:
                p = Proceso(pid, int(dur), int(pri))
                repo.agregar(p)
                print(f"Proceso {pid} agregado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == '2':
            procesos = repo.listar()
            if not procesos:
                print("No hay procesos registrados.")
            else:
                for p in procesos:
                    print(f"PID={p.pid}, duracion={p.duracion}, prioridad={p.prioridad}")

        elif opcion == '3':
            path = input("Ruta de archivo JSON/CSV: ").strip()
            try:
                if path.endswith('.json'):
                    repo.cargar_json(path)
                else:
                    repo.cargar_csv(path)
                print(f"Procesos cargados desde {path}.")
            except Exception as e:
                print(f"Error al cargar: {e}")

        elif opcion == '4':
            path = input("Ruta de salida JSON/CSV: ").strip()
            try:
                if path.endswith('.json'):
                    repo.guardar_json(path)
                else:
                    repo.guardar_csv(path)
                print(f"Procesos guardados en {path}.")
            except Exception as e:
                print(f"Error al guardar: {e}")

        elif opcion == '5':
            if not repo.listar():
                print("No hay procesos para planificar.")
                continue
            alg = input("Algoritmo (FCFS/RR): ").strip().upper()
            if alg not in ('FCFS','RR'):
                print("Algoritmo no válido.")
                continue
            quantum = 1
            if alg == 'RR':
                q = input("Quantum (int): ").strip()
                try:
                    quantum = int(q)
                except:
                    print("Quantum inválido, usando 1.")
            scheduler = FCFSScheduler() if alg == 'FCFS' else RoundRobinScheduler(quantum)
            gantt = scheduler.planificar(repo.listar())
            metrics = Metrics.from_gantt(gantt)
            print("Diagrama de Gantt:")
            for pid, ini, fin in gantt:
                print(f" {pid}: {ini} -> {fin}")
            print("Métricas medias:", metrics)

        elif opcion == '6':
            print("Saliendo...")
            return 0
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    sys.exit(main())