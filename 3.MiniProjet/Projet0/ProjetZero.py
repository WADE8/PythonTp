import os
import shutil
import logging

   

# Nom du fichier de log
log_file = 'monitoring.log'

def organiser_fichiers():

     # Configuration de base du logger
    logging.basicConfig(
        filename = log_file ,  
        # Le niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL), 
        # ici on enregistre tous les événements à partir de DEBUG
        level = logging.DEBUG,     
        datefmt = "%d-%m-%Y %H:%M",
        format = '%(asctime)s - %(levelname)s - %(message)s'  # Format de chaque message
    )

    # Demander à l'utilisateur d'entrer un nom de répertoire
    repertoire = input("Entrez le nom  du répertoire ")
    
    # Vérifier si le répertoire existe
    if not os.path.isdir(repertoire):

        os.makedirs(repertoire)
        
    else:
        logging.info(f"Chemin d'origine est : {os.path.abspath(repertoire)}")
         # Parcourir tous les fichiers du répertoire
        for nom_fichier in os.listdir(repertoire):
            chemin_complet = os.path.join(repertoire ,nom_fichier)
            
            
            # Identifier l'extension du fichier
            extension = os.path.splitext(nom_fichier)
            extension = extension[1].lstrip(".").upper()  # Supprimer le point et convertir en Majuscule
            
            # Créer le sous-dossier pour l'extension si nécessaire
            sous_dossier = os.path.join(repertoire, extension)
            if not os.path.exists(sous_dossier):
                os.makedirs(sous_dossier)
            
            # Déplacer le fichier dans le sous-dossier correspondant
            destination = os.path.join(sous_dossier, nom_fichier)
            logging.info(f"Chemin de destination {os.path.abspath(destination)}")

            shutil.move(chemin_complet, destination)
            logging.info(f"Deplacons le fichier {nom_fichier} de {os.path.abspath(repertoire)} vers {os.path.abspath(destination)}")
            


# Générer un rapport final
def generate_report():
    # Lire le fichier de log pour créer un rapport
    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    # Résumer les logs (compter le nombre d'occurrences par niveau)
    log_summary = {
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0,
    }
    
    for log in logs:
        if 'INFO' in log:
            log_summary['INFO'] += 1
        elif 'WARNING' in log:
            log_summary['WARNING'] += 1
        elif 'ERROR' in log:
            log_summary['ERROR'] += 1
        elif 'CRITICAL' in log:
            log_summary['CRITICAL'] += 1
    
    # Générer un rapport final
    report = (
        "Rapport des opérations\n"
        "======================\n"
        f"Total INFO : {log_summary['INFO']}\n"
        f"Total WARNING : {log_summary['WARNING']}\n"
        f"Total ERROR : {log_summary['ERROR']}\n"
        f"Total CRITICAL : {log_summary['CRITICAL']}\n"
    )


    # Sauvegarder le rapport dans un fichier
    with open('rapport_final.txt', 'w') as report_file:
        report_file.write(report)


if __name__ == '__main__':
    organiser_fichiers()
    generate_report()    