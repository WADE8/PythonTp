# Exercice 2 : Calcul de l'Age
from datetime import date

birthYearUser = input("Svp entrez votre annee de naissance")
yearCurrent = date.today()
age = yearCurrent.year - int(birthYearUser)
print("Vous etes age de :", age)