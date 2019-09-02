'''Compattazione di un vettore
Scrivere un programma in linguaggio Py che legge N numeri interi da tastiera e li memorizza in un vettore.
Il numero N viene inserito dall’utente ed è minore di 20.
Il programma deve generare un secondo vettore che compatta i numeri contenuti nel primo vettore.
In particolare:
• ogni numero che compare ripetuto nel primo vettore, deve comparire una sola volta nel secondo vettore
• ogni numero uguale a zero presente nel primo vettore non deve comparire nel secondo vettore.
Il programma deve visualizzare il contenuto del secondo vettore.

Esempio 1: si supponga N=8 e si consideri la sequenza di numeri 1 18 3 0 24 3 6 0 inseriti da tastiera.
Il programma deve visualizzare 1 18 3 24 6.

Esempio 2: si supponga N=10 e si consideri la sequenza di numeri 1 18 3 0 0 24 3 6 0 3 inseriti da tastiera.
Il programma deve visualizzare 1 18 3 24 6.
'''
# -----VARIABILI-----
array = []
n = 0
# -------------------
def nIns():
    global n
    print("Inserisci un valore > 0 < 20")
    while(n <= 0):
        try:
            n = int(input("Inserisci N:"))
            if(n <= 0 or n > 20):
                print("ERRORE. Inserisci un valore > di 0 e < 20")
                n = 0
        except ValueError:
            print("ERRORE. Valore inserito non corretto")

def stamp(vett,x):
    i = 0
    for i in range(x):
        print(vett[i],end=' ')
    print()

def memory(vett,x):
    i = 0
    elem = 0
    print("Inserisci",x,"elementi nell'array")
    while(i < x):
        print("Elemento",i+1,":",end='')
        try:
            elem = int(input())
            if(elem >= 0):
                vett.append(elem)
                i += 1
            else:
                print("ERRORE. Inserisci numeri interi positivi")
        except ValueError:
            print("ERRORE. Sono permessi solo numeri interi positivi\nRiprova")
    print("\nINGRESSO:",end=' ')
    stamp(vett,x)

def del0(vett,x):
    i = 0
    while(i < x):
        if(vett[i] == 0):
            del vett[i]
        else:
            i += 1
        if(x != len(vett) or x == x):
            x = len(vett)

def compatt(vett,x):
    del0(vett,x)
    i = 0
    app = 0
    while(i < x):
        j = 0
        app = vett[i]
        while(j < x):
            if(app == vett[j] and j != i):
                del vett[j]
            if(x != len(vett)):
                x = len(vett)
            j += 1
        i += 1
    print("COMPATTO:",end=' ')
    stamp(vett,x)

# -----MAIN-----
nIns()
memory(array,n)
compatt(array,n)
