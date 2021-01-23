# Création d'une fonction permettant de lister les applications du site.
# Les applications se trouvent dans le dossier applications.

from os import listdir
from os.path import isdir

def listing():
    """ Retourne tous les noms des applications créée. """
    dossier_applications = "./applications"
    fichiers = listdir(f"{dossier_applications}/")
    dossier = [f for f in fichiers if isdir(f"{dossier_applications}/{f}")]
    return dossier
    





