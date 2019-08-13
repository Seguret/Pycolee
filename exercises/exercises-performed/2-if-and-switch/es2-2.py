#Si scriva un programma in linguaggio Py che legga due numeri da tastiera,
#detti A e B, e determini le seguenti informazioni, stampandole a video:
#1. determini se B è un numero positivo o negativo
#2. determini se A è un numero pari o dispari
#3. calcoli il valore di A + B
#4. determini quale scelta dei segni nell’espressione (±A) + (±B)
# porta al risultato massimo, e quale è questo valore massimo.
#Suggerimento. Nel punto 4., il valore massimo della somma di A e B si può ottenere
# sommando il valore assoluto di A e di B.

#DICHIARAZIONE VARIABILI

a = 0
b = 0
c = 0

#-----------------------

a = float(input("inserisci un numero per A: "))
b = float(input("inserisci un numero per B: "))

if b > 0:
    print("B è positivo!")
elif b < 0:
    print("B è negativo!")
else:
    print("B è uguale a 0!")

if (a % 2) == 0:
    print("A è un numero pari!")
else:
    print("A è un numero dispari!")



print("la somma tra A e B è: " + str(a + b))

if a < 0:
    a = abs(a)

if b < 0:
    b = abs(b)

print("il valore massimo della somma +-A + +-B è uguale a: " + str(a+b))
