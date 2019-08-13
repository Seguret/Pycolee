#Data l’equazione
#                   ax + b = 0
#con a e b inseriti da tastiera, scrivere un programma in linguaggio Py
#per determinare il valore di x, se esiste, che risolve l’equazione.

#NOTA: x viene calcolata come x = -b/a

#-----VARIABILI-----

a = 0
b = 0
x = 0

#-------------------

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))

if a != 0:
    x = -b / a
    print("la soluzione è: ", str(x))
else:
    if b == 0:
        print("Equazione indeterminata (ammette infinite soluzioni)")
    else:
        print("Equazione Impossibile (non ammette soluzioni)")
