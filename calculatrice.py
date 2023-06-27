#####################################################
# Date : 10/03/2023
# Author : Amandine
#
# Descritption : Script  qui permet de faire des calculs arithmétiques standards
#                Addition, soustraction, division et multiplication
######################################################
#### Addition
nombre1 = 10
nombre2 = 20

total = nombre1 + nombre2

print("Resultat de l'addition = %d" % total)
print("%d + %d = %d" % (nombre1, nombre2, total))

#### Soustraction
nombre1 = 10
nombre2 = 20

total = nombre1 - nombre2

print("%d - %d = %d" % (nombre1, nombre2, total))

#### Division
nombre1 = 10
nombre2 = 20

total = nombre1 / nombre2

print("%d / %d = %d" % (nombre1, nombre2, total))

#### Multiplication
nombre1 = 10
nombre2 = 20

total = nombre1 * nombre2

print("%d * %d = %d" % (nombre1, nombre2, total))

#### FONCTION
def f_addition(nb1, nb2):
    total = nb1 + nb2
    return total

nb1 = 1020
nb2 = 3040

print("%d + %d -> Le resultat est" % (nb1, nb2), f_addition(nb1, nb2))

def f_soustraction(nb1, nb2):
    total = nb2 - nb1
    return total

nb1 = 1020
nb2 = 3040

print("%d - %d -> Le resultat est" % (nb2, nb1), f_soustraction(nb1, nb2))

def f_multiplication(nb1, nb2):
    total = nb1 * nb2
    return total

nb1 = 1020
nb2 = 3040

print("%d * %d -> Le resultat est" % (nb1, nb2), f_multiplication(nb1, nb2))

def f_division(nb1, nb2):
    total = nb2 / nb1
    return total

nb1 = 1020
nb2 = 3040

print("%d / %d -> Le resultat est" % (nb1, nb2), f_division(nb1, nb2))

###calculette automatique###

nb1 = str(input("Le premier nombre :"))
nb2 = str(input("Le second nombre :"))
choix = str(input("##OPTION CALCULETTE##"
                  "\n1=addition"
                  "\n2=soustraction"
                  "\n3=multiplactaion"
                  "\n4=division"
                  "\nChoisi quel calcul tu veux : "))


if choix == 1:
    print("Le résultat est égal à", f_addition(nb1, nb2))
elif choix == 2:
    print("Le résultat est égal à", f_soustraction(nb1, nb2))
elif choix == 3:
    print("Le résultat est égal à", f_multiplication(nb1, nb2))
elif choix == 4:
    print("Le résultat est égal à", f_division(nb1, nb2))