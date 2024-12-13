# Exercice 7: Compter les voyelles

#Demandons a l'utilisateur la phrase
phrase = input("Entrer une phrase ")

# Initialiser le compteur de voyelles
compteur_voyelles = 0

# Liste des voyelles
voyelles = "aeiouAEIOU"

# Parcourir chaque caractère de la phrase
for char in phrase:
  if( char in voyelles):
    compteur_voyelles +=1

# Afficher le nombre de voyelles
print(f"Le nombre de voyelles dans la phrase est : {compteur_voyelles}")