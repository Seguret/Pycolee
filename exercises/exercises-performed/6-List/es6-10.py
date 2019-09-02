'''Operazione di shift di un vettore

Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
Il valore N è inserito dall’utente.
I numeri sono memorizzati in un vettore.
Il programma esegue le seguenti operazioni:
    1. visualizza il vettore
    2. esegue uno spostamento (shift) a sinistra di una posizione del contenuto del vettore.
        Pertanto ogni elemento del vettore deve assumere il valore dell’elemento immediatamente
        successivo all’interno del vettore. L’elemento di indice N-1 deve assumere il valore zero.
        Ad esempio dato il vettore: 1 10 15 18
        Il programma deve generare il vettore: 10 15 18 0
        Il programma visualizza il vettore ottenuto.
    3. esegue uno spostamento (shift) a destra di una posizione del contenuto del vettore ottenuto
        nel passo precedente. Pertanto ogni elemento del vettore deve assumere il valore dell’elemento
        immediatamente precedente all’interno del vettore. L’elemento di indice 0 deve assumere il valore zero.
        Ad esempio dato il vettore: 10 15 18 0
        Il programma deve generare il vettore: 0 10 15 18
        Il programma visualizza il vettore ottenuto.

Nota. Nella definizione di “destra” e “sinistra” si immagini il vettore stampato orizzontalmente,
a partire dalla cella di indice 0.
'''
# -----VARIABILI-----
n = 0
array = []
s = 0
# -------------------
def nIns():
    global n
    while(n <= 0):
        try:
            n = int(input("Inserisci un valore N: "))
            if(n <= 0):
                print("ERRORE. Inserire un valore maggiore di 0")
                n = 0
        except ValueError:
            print("ERRORE. Valere non concesso")

def stamp(vett,x):
    i = 0
    for i in range(x):
        print(vett[i], end=' ')

def memory(vett,x):
    i = 0
    app = 0
    print("\ninserisci",x,"elementi nell'array")
    while(i < x):
        try:
            print("Elemento",i+1,":",end='')
            app = int(input())
            if(app < 0):
                print("ERRORE. Inserisci un valore intero maggiore di 0")
            else:
                vett.append(app)
                i += 1
        except ValueError:
            print("ERRORE. Valore inserito non concesso")
    stamp(vett,x)

def sx(vett, x):
    i = 0
    j = 1
    print("              Ingresso: ",end='')
    stamp(vett,x)
    while(j < x):
        vett[i] = vett[j]
        j += 1
        i += 1
    if(j == x):
        vett[j-1] = 0
    print("\nSpostamento a Sinistra: ",end='')
    stamp(vett,x)

def dx(vett, x):
    i = x-1
    j = x-2
    print("            Ingresso: ",end='')
    stamp(vett,x)
    while(j >= 0):
        vett[i] = vett[j]
        j -= 1
        i -= 1
    if(j < 0):
        vett[0] = 0
    print("\nSpostamento a Destra: ",end='')
    stamp(vett,x)

# -----MAIN-----
nIns()
memory(array,n)

print("\n\nSeleziona il tipo di spostamento\n1: sinistra\n2: destra")
s = int(input())
if(s == 1):
    sx(array,n)
elif(s == 2):
    dx(array, n)
