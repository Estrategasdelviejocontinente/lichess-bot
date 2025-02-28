#!/bin/bash

# Crear un entorno virtual en .venv
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Actualizar pip dentro del venv
pip install --upgrade pip

# Instalar dependencias en el entorno virtual
pip install -r requirements.txt
