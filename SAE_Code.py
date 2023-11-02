import os
import importlib
import subprocess
import sys

try:
    importlib.import_module("keyboard")
except ImportError:
    print("La bibliothèque keyboard n'est pas installée. Installation en cours...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard'])
    except Exception as e:
        print(f"Erreur lors de l'installation de keyboard : {e}")
        sys.exit(1)
