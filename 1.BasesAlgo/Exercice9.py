# Exercice 9: Palindrome

#Demandons a l'utilisateur un mot
chaine = input("Entrer un mot ")

if chaine == chaine[::-1]:
  print("Votre mot est un palindrome")

else:
  print("Votre mot n'est pas un palindrome")