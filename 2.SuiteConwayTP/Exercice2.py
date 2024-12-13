# Deinition de la fonction premierMot
def premierMot(chaineDeCaractere):
  # Diviser la chaîne en une liste de mots
  mots = chaineDeCaractere.split()
  print(f"Le premier mot est : {mots[0]}")


if __name__ == '__main__':
  chaineDeCaractere = input("Entrer la chaine de caracteres")
  premierMot(chaineDeCaractere)