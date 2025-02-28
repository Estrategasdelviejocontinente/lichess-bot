import os
import sys
import subprocess

# Ruta del entorno virtual
venv_path = ".venv"

# Si el entorno virtual no existe, lo creamos
if not os.path.exists(venv_path):
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", venv_path])

# Asegurar que estamos usando el `pip3` dentro del entorno virtual
pip_bin = os.path.join(venv_path, "bin", "pip3")

# Si no existe pip3 en el entorno virtual, vamos a instalarlo
if not os.path.exists(pip_bin):
    print("pip3 no encontrado, instalando pip...")
    subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"])

# Ahora instalamos 'chess' si no está instalado
try:
    import chess
except ModuleNotFoundError:
    print("Instalando módulo 'chess' con pip3...")
    subprocess.run([pip_bin, "install", "chess"])
    import chess  # Intentamos importar de nuevo después de instalar

# Ahora ejecutamos el bot normalmente
from lib.lichess_bot import start_program


if __name__ == "__main__":
    start_program()
