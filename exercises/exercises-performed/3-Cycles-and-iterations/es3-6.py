#Si scriva un programma in linguaggio Py per calcolare la media aritmetica di una serie di
#numeri inseriti da tastiera. L’introduzione tramite il valore "exit"
#indica il termine del caricamento dei dati.

# -----VARIABILI-----

somma = 0
x = 0
count = 0

# -------------------

while x != "exit":
    x = input("inserisci valore: ")
    if x != "exit":
        somma = somma + int(x)
        count = count + 1


print(somma/count)
