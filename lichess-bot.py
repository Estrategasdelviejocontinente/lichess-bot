import os
import sys
import subprocess

# Ruta del entorno virtual
venv_path = ".venv"

# Si el entorno virtual no existe, lo creamos
if not os.path.exists(venv_path):
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", venv_path])

# Asegurar que usamos el Python del venv
python_bin = os.path.join(venv_path, "bin", "python")

# Instalar paquetes dentro del venv si es necesario
try:
    import chess
except ModuleNotFoundError:
    print("Instalando módulo 'chess'...")
    subprocess.run([python_bin, "-m", "pip", "install", "chess"])
    import chess  # Volver a importar después de instalar

# Ahora ejecutamos el bot

from lib.lichess_bot import start_program

if __name__ == "__main__":
    start_program()
