from pdf2image import convert_from_path
import os
import time

def convert_pdf_to_images(pdf_path):
    # Extraire le nom du fichier sans l'extension pour nommer le dossier de sortie
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = f"{base_filename}"
    
    # Créer le dossier de sortie
    os.makedirs(output_folder, exist_ok=True)
    print(f"Dossier de sortie : {output_folder}")

    try:
        # Démarrer le chronométrage
        start_time = time.time()
        
        # Convertir le PDF en une liste d'images
        print(f"Conversion du fichier PDF : {pdf_path}")
        images = convert_from_path(pdf_path, dpi=200, fmt="png") # dpi max = 500
        print(f"Nombre d'images converties : {len(images)}")

        # Sauvegarder chaque image avec un nom de fichier formaté avec 3 chiffres
        image_paths = []
        for i, image in enumerate(images, start=1):
            # Formatage des numéros de pages avec 3 chiffres
            image_name = f"{i:03}.png"
            image_path = os.path.join(output_folder, image_name)
            image.save(image_path, "PNG")
            image_paths.append(image_path)
            print(f"Image sauvegardée : {image_path}")
        
        # Calculer et afficher le temps écoulé
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Temps total de conversion : {elapsed_time:.2f} secondes")

        return image_paths
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return []

# Nom du fichier PDF à convertir
pdf_path = "pdf/test.pdf"

# Vérifier si le fichier PDF existe avant de lancer la conversion
if os.path.exists(pdf_path):
    images = convert_pdf_to_images(pdf_path)
    if images:
        print("Images converties :", images)
    else:
        print("Aucune image n'a été convertie.")
else:
    print(f"Erreur : fichier PDF introuvable -> {pdf_path}")
