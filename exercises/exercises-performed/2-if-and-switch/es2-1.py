#Si realizzi un programma in linguaggio Py che acquisisca da
#tastiera un numero e stampi un messaggio che indichi se
#tale numero sia positivo oppure negativo e stampi il valore assoluto di tale numero.

import math

#DICHIARAZIONE VARIABILI

x = 0

#-----------------------

x = float(input("inserisci un valore X: "))

if x > 0:
    print("Il valore è positivo")
elif x == 0:
    print("il valore è uguale a 0")
else:
    print("il valore è negativo")
    x = abs(x)
    print("il valore assoluto di X è: " + str(x))
