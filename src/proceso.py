class Proceso:
    """
    Representa un proceso del sistema.

    Atributos:
        pid (str): Identificador único, no vacío.
        duracion (int): Tiempo de CPU requerido, entero positivo.
        prioridad (int): Prioridad del proceso, entero (menor = más urgente).
        tiempo_restante (int): Para uso interno del scheduler.
        tiempo_llegada (int): Asumido 0.
        tiempo_inicio (Optional[int]): Tiempo de inicio de ejecución.
        tiempo_fin (Optional[int]): Tiempo de fin de ejecución.
    """
    _pids_registrados = set()

    def __init__(self, pid: str, duracion: int, prioridad: int):
        # Validación de PID
        if not isinstance(pid, str) or not pid.strip():
            raise ValueError("El PID debe ser un string no vacío.")
        if pid in Proceso._pids_registrados:
            raise ValueError(f"PID '{pid}' ya existe.")
        # Validación de duración
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        # Validación de prioridad
        if not isinstance(prioridad, int) or prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None

        # Registrar PID
        Proceso._pids_registrados.add(pid)

    @staticmethod
    def resetear_registro():
        """Resetea el registro de PIDs (para pruebas)."""
        Proceso._pids_registrados.clear()
class Proceso:
    """
    Representa un proceso del sistema.
    """
    _pids_registrados = set()

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if pid in Proceso._pids_registrados:
            raise ValueError(f"PID '{pid}' ya existe.")
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None
        Proceso._pids_registrados.add(pid)

    @staticmethod
    def resetear_registro():
        """Resetea el registro de PIDs (para pruebas)."""
        Proceso._pids_registrados.clear()