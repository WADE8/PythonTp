import pandas as pd
import re
import matplotlib.pyplot as plt
from faker import Faker
import random
import csv
from datetime import datetime, timedelta

# Generons un fichier le log d'acces web grace aFaker

# Initialisation de Faker
fake = Faker()

# Liste des méthodes HTTP et codes de statut
methods = ['GET', 'POST', 'PUT', 'DELETE']
urls = ['/home', '/login', '/admin', '/contact']
statuses = [200, 404, 500, 301]

#Fonction qui prend en parametre le nombre de logs  
# et les enregistre dans un fichier CSV

def generer_logs_csv(n):
    with open('logs.csv', 'w', newline='') as csvfile:
        fieldnames = ['ip', 'datetime', 'method', 'url', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for _ in range(n):
            ip = fake.ipv4()  # Générer une adresse IP
            method = random.choice(methods)
            url = random.choice(urls)
            status = random.choice(statuses)
            datetime_str = (datetime.now() - timedelta(minutes=random.randint(1, 1000))).strftime('%Y-%m-%d %H:%M:%S')
            
            
         
            # Écrire le log dans le fichier CSV
            writer.writerow({'ip': ip, 'datetime': datetime_str, 'method': method, 'url': url, 'status': status})


# 1.Importer notre fichier de logs d'accès web (format CSV)
def importer_logs(fichier):
    logs = pd.read_csv(fichier)
    return logs


# 2. Analyser les logs pour identifier des schémas suspects
def analyser_logs(logs):
    # Tentatives de connexion répétées (exemple : /login ou /admin)
    logs['tentatives_connexion'] = logs['url'].apply(lambda x: bool(re.search(r'/login|/admin', x)))
    
    # Tentatives répétées de la même adresse IP
    # On compte le nombre de requete par ip .
    # Si une IP effectue plus de 5 requêtes, elle est marquée comme suspecte.
    logs['ip_repetitive'] = logs.groupby('ip')['ip'].transform('count') > 5  

    # Rechercher des accès fréquents à des pages 404
    logs['tentatives_404'] = (logs['status'] == 404)
    
    return logs


# 3. Visualiser les adresses IP les plus fréquentes et les types de requêtes
def visualiser_ip_requetes(logs):
    # Compter les adresses IP les plus fréquentes
    ip_frequentes = logs['ip'].value_counts().head(10)
    
    # Visualiser les IP les plus fréquentes
    plt.figure(figsize=(10, 6))
    ip_frequentes.plot(kind='bar', color='skyblue')
    plt.title("Top 10 des adresses IP les plus fréquentes")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre de requêtes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Compter les types de réponses HTTP (status codes)
    status_codes = logs['status'].value_counts()

    # Visualiser les types de réponses HTTP
    plt.figure(figsize=(10, 6))
    status_codes.plot(kind='bar', color='salmon')
    plt.title("Répartition des codes de statut HTTP")
    plt.xlabel("Code HTTP")
    plt.ylabel("Nombre de requêtes")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# 4. Générer un rapport des IP suspectes
def generer_rapport_ip_suspectes(logs):
    # Sélectionner les IP suspectes (par exemple, celles avec plus de 5 requêtes ou des tentatives sur /login /admin)
    ip_suspectes = logs[(logs['ip_repetitive']) | (logs['tentatives_connexion'])]
    
    # Créer un rapport sous forme de fichier CSV
    ip_suspectes.to_csv('ip_suspectes.csv', index=False)
    print("Le rapport des IP suspectes a été généré : 'ip_suspectes.csv'")



if __name__ == '__main__':

    # On appelle la fonction generer_logs_csv dans le main 
    # pour generer 80 logs dans notre fichier logs.cvs
    generer_logs_csv(80)

    # On charge le fichier log.csv dans un DataFrame Pandas
    logs = importer_logs('D:\MiniProjet\Projet1\logs.csv')

    # Analyser les logs pour identifier des schémas suspects
    logs_analyzes = analyser_logs(logs)

    # Visualiser les résultats
    visualiser_ip_requetes(logs_analyzes)

    # Générer un rapport des IP suspectes
    generer_rapport_ip_suspectes(logs_analyzes)


