# Exercice 4 : Somme des nombres
# Boucle For (Pour faire la somme de 1 au nombre)
nombre = int(input("Entrer un nombre svp!!"))
somme = 0
for i in range(1,nombre+1):
  somme += i

print("La somme est: ",somme)