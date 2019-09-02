'''Ricerca di un elemento in vettore
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
I numeri sono memorizzati in un vettore.
Il valore N è inserito dall’utente, ma il vettore può contenere al massimo 30 numeri.

Terminato l’inserimento della sequenza di numeri, l’utente inserisce un valore di riferimento.
Il programma deve indicare se tale valore di riferimento è contenuto nel vettore.
'''

# -----VARIABILI-----
n = 0
# -------------------
def nInteri():
    global n
    length = 30
    while(n <= 0):
        try:
            n = int(input("Inserisci N:"))
            if(n > length):
                print("ERRORE. Non c'è spazio per ",n, "elementi.")
                n = 0
            elif(n <= 0):
                print("ERRORE. Inserisci un numero intero positivo > 0")
        except ValueError:
            print("ERRORE. Inserisci un numero intero positivo <= 30")
    return n

def memory(x):
    i = 0
    array = []
    elem = 0
    print("Inserisci ", x, "numeri interi")
    for i in range(x):
        print("elemento della Lista numero ", i, ":", end='')
        elem = int(input())
        array.append(elem)
    return array

def search(arr, x):
    ser = False
    r = i = 0
    count = 0
    found = []
    r = int(input("Inserisci il valore da ricercare: "))
    for i in range(x):
        if(arr[i] == r):
            found.append(i+1)
            ser = True
    if(ser == False):
        print("Elemento non presente nella lista.")
    else:
        count = len(found)
        print("\nElemento TROVATO.\n E' presente ", len(found), "volte nelle posizioni ", found)

# -----MAIN-----

f = nInteri()
vett = memory(f)
search(vett, f)

