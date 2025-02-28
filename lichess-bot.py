import os
import sys
import subprocess

# Ruta del entorno virtual
venv_path = ".venv"

# Si el entorno virtual no existe, lo creamos
if not os.path.exists(venv_path):
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", venv_path])

# Asegurar que usamos `python3` y `pip3` dentro del entorno virtual
python_bin = os.path.join(venv_path, "bin", "python3")
pip_bin = os.path.join(venv_path, "bin", "pip3")

# Si `pip3` no existe, usar `pip`
if not os.path.exists(pip_bin):
    pip_bin = os.path.join(venv_path, "bin", "pip")

# Instalar paquetes dentro del venv si es necesario
try:
    import chess
except ModuleNotFoundError:
    print("Instalando módulo 'chess' con pip3...")
    subprocess.run([pip_bin, "install", "chess"])
    import chess  # Volver a importar después de instalar

# Ahora ejecutamos el bot normalmente
from lib.lichess_bot import start_program

if __name__ == "__main__":
    start_program()
