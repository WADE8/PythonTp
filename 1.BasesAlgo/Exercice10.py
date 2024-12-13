# Exercice 10: Factorielle

nombre = int(input("Entrer un nombre svp!! "))

def factorielle(nombre):

  if nombre < 0:
     return "La factorielle n'est pas définie pour les nombres négatifs"

  if nombre == 0 or nombre == 1:
        return 1
  else:
    return nombre * factorielle(nombre-1)

print(f"Le factoriel du nombre {nombre} est", factorielle(nombre))