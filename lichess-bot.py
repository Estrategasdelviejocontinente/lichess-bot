"""Starting point for lichess-bot."""
import subprocess
import sys

# Intentar instalar el paquete chess
subprocess.check_call([sys.executable, "-m", "pip", "install", "chess"])

# Ahora importar el paquete
import chess

from lib.lichess_bot import start_program

from lib.lichess_bot import start_program

if __name__ == "__main__":
    start_program()
