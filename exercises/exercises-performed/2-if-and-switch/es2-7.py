#Si scriva un programma in linguaggio Py che acquisisca due numeri interi da tastiera e:
#• determini, stampando un messaggio opportuno quale dei due numeri (il primo o il secondo) sia maggiore
#• stampi il valore di tale numero.

# -----VARIABILI-----

a = 0
b = 0

# -------------------

a = int(input("inserisci un valore per A: "))
b = int(input("inserisci un valore per B: "))

if a > b:
    print("\nIl maggiore è: ", a)
else:
    print("\nIl maggiore è: ", b)

