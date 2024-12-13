#Retourne une phrase

def retourner_phrase(phrase):
  # Diviser la phrase en mots
  mots = phrase.split()
  # Inverser l'ordre des mots
  mots_inverses = mots[::-1]
  #rejoindre les mots inverses
  return ' '.join(mots_inverses)


if __name__ == '__main__':
  chaine_de_caracteres = input("Entrer une chaine de caractere ")
  print(retourner_phrase(chaine_de_caracteres ))