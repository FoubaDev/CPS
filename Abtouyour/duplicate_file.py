#!/usr/bin/python3

import shutil
import os

def dupliquer_fichier(source_file, destination_folder, n):
    # Vérifier si le fichier source existe
    if not os.path.exists(source_file):
        print(f"Le fichier {source_file} n'existe pas.")
        return
    
    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Extraire le nom de fichier et son extension
    file_name, file_extension = os.path.splitext(os.path.basename(source_file))

    # Copier le fichier n fois
    for i in range(1, n + 1):
        new_file_name = f"{file_name}_{i}{file_extension}"
        new_file_path = os.path.join(destination_folder, new_file_name)
        shutil.copy(source_file, new_file_path)

# Exemple d'utilisation
source_file = "/home/fouba/Documents/CPS_Technicien/Data_Cleaning/Abtouyour/Walia-Est.xls"
destination_folder = "/home/fouba/Documents/CPS_Technicien/Data_Cleaning/Walia-Est/"
n = 25  # Nombre de duplications
dupliquer_fichier(source_file, destination_folder, n)

