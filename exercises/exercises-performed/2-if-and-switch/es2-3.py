#Si scriva un programma in linguaggio Py che legga da tastiera i valori
#delle lunghezze dei tre lati di un triangolo (detti A, B e C), e determini:
#• se il triangolo è equilatero
#• se il triangolo è isoscele
#• se il triangolo è scaleno
#• se il triangolo è rettangolo.

#----VARIABILI----

a = 0
b = 0
c = 0

#-----------------

a = float(input("inserisci il lato A: "))
b = float(input("inserisci il lato B: "))
c = float(input("inserisci il lato C: "))

if a == b == c:
    print("Equilatero!")
elif a==b or b==c or a==c:
    print("Isoscele!")
elif a!=b and b!=c and a!=c:
    print("Scaleno!")

if a*a == b*b + c*c:
    print("Il triangolo è rettangolo!")
else:
    print("Il triangolo non è rettangolo!")
