
def image(mot):
    resultat = []
    count = 1  # On commence avec un comptage de 1
    # On parcourt chaque caractère du mot, à l'exception du dernier
    for i in range(1, len(mot)):
        if mot[i] == mot[i - 1]:
            count += 1  # On incrémente le compteur si le caractère est le même que le précédent
        else:
            resultat.append(str(count) + mot[i - 1])  # On ajoute le résultat pour la séquence précédente
            count = 1  # Réinitialiser le compteur
    # Ajouter le dernier groupe
    resultat.append(str(count) + mot[-1])
    return ''.join(resultat)

def suite(n):
    u = '1'  # Terme de départ
    for _ in range(n):
        print(u)  # Afficher le terme courant
        u = image(u)  # Passer au terme suivant

# Afficher les 20 premiers termes de la suite
suite(20)

