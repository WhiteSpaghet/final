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