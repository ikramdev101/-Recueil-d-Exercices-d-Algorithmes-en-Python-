# LES EXERCICE D'application :

# EXERCICE 1 :

def factor(n):
    if n < 0 :
        print("erreur")
    if n == 0 :
        print("le factoriel de 0 est 1 .")
    if n > 0 :
        f = 1
        for i in range(1,n+1):
            f = f*i
        print("le factoriel est egale à :",f)

n=int(input("svp saisir un entier N :"))
factor(n)


# EXERCICE 2 :

def verif(chain):
    chain = chain.lower()
    if chain == chain[::-1]:
        print("votre chaine est palindrom")
    else:
        print("votre chaine n'est pas palindrom")

chain=(input("svp saisir une chaine :"))
verif(chain)

# EXERCICE 3 :

def validate_email(chaine):
    if "@ ." in chaine:
        print("votre forme email est correct")
    else:
        print("votre forme est incorrect")
chaine=(input("svp saisir une chaine  :"))
validate_email(chaine)
 
# EXERCICE 4 :

def dessin(n):
    if N < 0 :
        print("erreur")
    else:
        for i in range(1,N+1):
            print(" "*(N-i),end="")
            print(""(2*i-1))

N=int(input("svp saisir un entier N :"))
dessin(N)

# EXERCICE 5 :
def calcul(c,chaine): 
    l=0
    for i in chaine:
        if i == c :
            l+=len(c)
    print("le nombre de repetition de la litre ",c,"est",l)
chaine=input("svp saisir une chaine  :")
c =input("svp saisir le caracter a chercher ")
calcul(c,chaine)

# EXERCICE 6 :

def moyenne_liste(L):
    som =0
    moy=0
    for i in L :
        som+=i
        moy=som/len(L)
    print('le moyenne est ',moy)

L = [-2,5.3,6.7]
moyenne_liste(L)


#  EXERCICE 7 :

def occurrences_and_positions(l, element):
    nombre_occurrences = 0
    premiere_occurrence = None
    derniere_occurrence = None

    for i, valeur in enumerate(l):
        if valeur == element:
            nombre_occurrences += 1
            if premiere_occurrence is None:
                premiere_occurrence = i
            derniere_occurrence = i

    return nombre_occurrences, premiere_occurrence, derniere_occurrence

l = [1, 2, 3, 2, 4, 2, 5]
element_recherche = 2
occurrences, premiere, derniere = occurrences_and_positions(l, element_recherche)

print("Nombre d'occurrences de", element_recherche, ":", occurrences)
print("Position de la première occurrence :", premiere)
print("Position de la dernière occurrence :", derniere)


#  EXERCICE 8 :
def trier_liste(l):
    l.sort()

l = [ -4,5, 2, 8, 1, 3]
trier_liste(l)
print("Liste triée dans l'ordre croissant :", l)

#  EXERCICE 9 :

def supp_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    nouvelle_chaine = ""
    for char in chaine:
        if char not in voyelles:
            nouvelle_chaine += char
    print("Votre chaîne après suppression des voyelles est :", nouvelle_chaine)

chaine = input("Veuillez saisir une chaîne : ")
supp_voyelles(chaine)

#  EXERCICE 10 :

def isPerfect(nombre):
    somme_diviseurs = 0
    for i in range(1, nombre):
        if nombre % i == 0:
            somme_diviseurs += i
    return somme_diviseurs == nombre

nombre =int(input("svp saisir un entier :"))
if  isPerfect(nombre):
    print(nombre, "est un nombre parfait.")
else:
    print(nombre, "n'est pas un nombre parfait.")


#  EXERCICE 11 :

def insert_string(chaine, n, c):
    nouvelle_chaine = chaine[:n] + c + chaine[n:]
    print("Votre chaîne après les modifications est :", nouvelle_chaine)

chaine = input("Veuillez saisir une chaîne : ")
c = input("Veuillez saisir le caractère à insérer : ")
n = int(input("Veuillez saisir la position d'insertion du caractère : "))
insert_string(chaine, n, c)