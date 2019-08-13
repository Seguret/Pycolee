#Si scriva un programma in linguaggio Py che acquisisca un numero intero positivo N da tastiera
#e stampi il valore del fattoriale di N.
#Suggerimento. Si ricorda che il fattoriale di un numero è il prodotto di
#tutti i numeri compresi tra 1 ed N.

# -----VARIABILI-----

n = 0

# -------------------

def fattoriale(x):
    i = 1
    j = x
    while i < j:
        x = x * i
        i = i + 1
    print(x)


n = int(input("Inserisci un valore per N: "))

fattoriale(n)

