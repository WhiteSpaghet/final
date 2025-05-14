#!/usr/bin/env python3
"""
Launcher de la aplicación de simulación de planificación de CPU.
Define cómo iniciar la función main de src/main.
"""
import sys
from src.main import main as cli_main

def launch():
    """Lanza la CLI y gestiona el código de salida."""
    exit_code = cli_main()
    sys.exit(exit_code)