import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration du logging
logging.basicConfig(filename='file_changes.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# Classe de gestion des événements de surveillance des fichiers
class FileChangeHandler(FileSystemEventHandler):

    def __init__(self, event_list):
        self.event_list = event_list

    def on_modified(self, event):
        #On ignore les events sur les dossiers
        if not event.is_directory:
            #Heure et la date de la modification
            event_time = datetime.now()
            # Enregistrer l'événement dans le fichier de log
            logging.info(f'Fichier {__file__} a ete modifié: {event.src_path}')
            # Ajouter l'événement à la liste pour le graphique
            self.event_list.append(event_time)

    def on_created(self, event):
        if not event.is_directory:
            #Heure et la date de la creation 
            event_time = datetime.now()
            # Enregistrer l'événement dans le fichier de log
            logging.info(f'Fichier {__file__} a ete crée: {event.src_path}')
            # Ajouter l'événement à la liste pour le graphique
            self.event_list.append(event_time)
    
    def on_deleted(self, event):
        if not event.is_directory:
            #Heure et la date de la suppression
            event_time = datetime.now()
            # Enregistrer l'événement dans le fichier de log
            logging.info(f'Fichier {__file__} a ete supprimé: {event.src_path}')
            # Ajouter l'événement à la liste pour le graphique
            self.event_list.append(event_time)

  
#Fonction pour surveiller en permanence le repertoire    
# qui prend en parametre le repertoire
def start_watching(directory):
    event_list = []
    event_handler = FileChangeHandler(event_list)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Surveillance du répertoire {directory} en cours. Appuyez sur Ctrl+C pour arrêter.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print("Surveillance arrêtée.")
        return event_list


def plot_events(event_list):
    # Convertir les événements en un format temporel
    event_times = [event.strftime('%H:%M:%S') for event in event_list]
    
    # Compter les occurrences de chaque heure (ou minute si nécessaire)
    time_count = {time: event_times.count(time) for time in set(event_times)}
    
    # Trier les événements par heure
    sorted_times = sorted(time_count.items())

    plt.figure(figsize=(10, 5))
    plt.bar([item[0] for item in sorted_times], [item[1] for item in sorted_times])
    plt.xlabel('Heure de modification')
    plt.ylabel('Nombre d\'événements')
    plt.title('Événements de modification de fichiers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()        


if __name__ == "__main__":
    directory_to_watch = "./DirectoryOne"  
    events = start_watching(directory_to_watch)
    plot_events(events)