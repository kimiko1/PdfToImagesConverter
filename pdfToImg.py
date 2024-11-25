from pdf2image import convert_from_path
import os
import time
from termcolor import colored

def convert_pdf_to_images(pdf_path):
    """
    Convertit un fichier PDF en images PNG, une image par page, et les sauvegarde dans un dossier dédié.
    """

    # Extraire le nom du fichier sans l'extension pour créer le nom du dossier de sortie
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = f"{base_filename}"

    # Créer le dossier de sortie si il n'existe pas
    os.makedirs(output_folder, exist_ok=True)
    print(colored(f"Dossier de sortie créé : {output_folder}", "green"))

    try:
        # Démarrer le chronométrage de la conversion
        start_time = time.time()
        print(colored(f"Conversion du fichier PDF : {pdf_path}", "cyan"))

        # Convertir le PDF en images avec une résolution DPI de 500
        images = convert_from_path(pdf_path, dpi=10, fmt="png")
        print(colored(f"Nombre d'images converties : {len(images)}", "yellow"))

        # Sauvegarder chaque image dans le dossier de sortie
        image_paths = []
        for i, image in enumerate(images, start=1):
            # Nom de l'image avec un format à 3 chiffres pour la numérotation
            image_name = f"{i:03}.png"
            image_path = os.path.join(output_folder, image_name)
            
            # Sauvegarder l'image au format PNG
            image.save(image_path, "PNG")
            image_paths.append(image_path)
            print(colored(f"Image sauvegardée : {image_path}", "magenta"))
        
        # Calcul du temps total écoulé pour la conversion
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(colored(f"Temps total de conversion : {elapsed_time:.2f} secondes", "green"))

        return image_paths

    except Exception as e:
        print(colored(f"Erreur lors de la conversion : {e}", "red"))
        return []

def convert_pdfs_in_folder(folder_path):
    """
    Convertit tous les fichiers PDF dans un dossier en images PNG.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            if os.path.exists(pdf_path):
                images = convert_pdf_to_images(pdf_path)
                if images:
                    print(colored("Images converties :", "blue"), images)
                else:
                    print(colored("Aucune image n'a été convertie.", "yellow"))
            else:
                print(colored(f"Erreur : fichier PDF introuvable -> {pdf_path}", "red"))

# Chemin du dossier contenant les fichiers PDF à convertir
folder_path = "pdf"

# Vérifier si le dossier existe avant de lancer la conversion
if os.path.exists(folder_path):
    convert_pdfs_in_folder(folder_path)
else:
    print(colored(f"Erreur : dossier introuvable -> {folder_path}", "red"))