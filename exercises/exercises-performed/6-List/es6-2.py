'''Conversione Binario-Decimale
Si scriva un programma in linguaggio Py che converta un numero binario in un numero decimale.
Il numero binario è rappresentato su N bit, e il valore di N è inserito da tastiera.
L’utente inserisce le cifre del numero binario un bit alla volta, partendo dal bit meno significativo
(ossia dal bit di peso 20).
Il programma visualizzerà il numero decimale corrispondente.
Gestire tutti gli errori di inserimento.

Suggerimento. Per calcolare le potenze di 2 utilizzare la funzione pow, includendo la libreria math.h.
Ad esempio per calcolare 25, si scriverà pow(2,5). In generale, data una base a, per calcolare y = ab,
si scrive y = pow(a,b) includendo la libreria math.h.
'''

import math
# -----VARIABILI-----
lista=[]
i = 0
bit = 0
n = 0
# -------------------

def inser(bina, elem):
    bina.append(elem)

def conversione(bina):
    global n
    decimale = 0
    expo = 0
    j = n - 1
    while(j >= 0):
        if(bina[j]==1):
            decimale = decimale + (bina[j]*pow(2,expo))
        expo = expo + 1
        j = j - 1
    print(bina)
    print(decimale)

# -----MAIN-----
while(n <= 0):
    try: #il try è stato inserito per gestire gli errori di inserimento (es. stringhe, null)
        n = int(input("Inserisce il numero di bit: "))
        if(n <= 0):
            print("ERRORE. Inserire un valore > di 0")
    except ValueError:
        print("ERRORE. \n Riprova")

while(i < n):
    try:
        print("inserisci il bit num ", i, ": ")
        bit = int(input(),2)
        inser(lista, bit)
        i = i + 1
    except ValueError: #mentre questo try è per gestire tutti i valori inseriti diversi da 0 e 1
        print("ERRORE.")

lista.reverse()
conversione(lista)
