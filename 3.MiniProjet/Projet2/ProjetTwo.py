import socket
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

# Fonction pour tester si un port est ouvert
def tester_port(ip, port):
    try:
        # Création de la connexion socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout de 1 seconde pour éviter les blocages
            s.connect((ip, port))
        return port, True
    except (socket.timeout, socket.error):
        return port, False


# Fonction principale de scan de ports
def scanner_ports(ip, ports):
    # Liste pour stocker les ports ouverts
    ports_ouverts = []

    # Utilisation de ThreadPoolExecutor pour paralléliser les tests
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda port: tester_port(ip, port), ports)
    
    # Collecte des résultats
    for port, ouvert in results:
        if ouvert:
            ports_ouverts.append(port)
    
    return ports_ouverts


# Fonction pour afficher les résultats sous forme de graphique
def afficher_graphique(ports_ouverts):
    # Création d'un graphique à barres
    
    plt.bar(ports_ouverts, [1] * len(ports_ouverts),10,color='skyblue')
    plt.xlabel('Ports')
    plt.ylabel('État (ouvert)')
    plt.title('Ports ouverts sur la machine cible')
    plt.show()



# Lancer le script
if __name__ == "__main__":
    # Demande à l'utilisateur l'IP cible
    ip = input("Entrez l'adresse IP de la cible : ")
    # Liste des ports à scanner
    ports = range(1, 1025)  

    # Scanner les ports
    print(f"Scanning des ports sur {ip}...")
    ports_ouverts = scanner_ports(ip, ports)

    # Afficher les résultats
    if ports_ouverts:
        print(f"Ports ouverts sur {ip} : {ports_ouverts}")
        afficher_graphique(ports_ouverts)
    else:
        print(f"Aucun port ouvert trouvé sur {ip}.")