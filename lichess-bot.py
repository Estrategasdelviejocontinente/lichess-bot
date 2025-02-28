import os
import sys
import subprocess

# Ruta del entorno virtual
venv_path = ".venv"

# Si el entorno virtual no existe, lo creamos
if not os.path.exists(venv_path):
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", venv_path])

# Activar el entorno virtual
activate_script = os.path.join(venv_path, "bin", "activate_this.py")
if os.path.exists(activate_script):
    exec(open(activate_script).read(), dict(__file__=activate_script))
    print("Entorno virtual activado.")

# Asegurar que `chess` está instalado
try:
    import chess
except ModuleNotFoundError:
    print("Instalando módulo 'chess'...")
    subprocess.run([f"{venv_path}/bin/pip", "install", "chess"])
    import chess  # Volver a importar después de instalar

# Ahora ejecutamos el bot normalmente
from lib.lichess_bot import start_program


from lib.lichess_bot import start_program

if __name__ == "__main__":
    start_program()
