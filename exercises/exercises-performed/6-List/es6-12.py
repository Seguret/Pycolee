'''Intersezione di due vettori
Siano dati due vettori di interi inseriti da tastiera.
La lunghezza dei due vettori è inserita dall’utente da tastiera.
I due vettori possono avere lunghezze diverse, ma possono contenere al massimo 30 numeri.
Si scriva un programma in linguaggio Py per generare un terzo vettore che contiene l’intersezione
tra due vettori. Tale vettore deve contenere i numeri presenti in entrambi i vettori dati.
Ad esempio, si assuma che siano stati inseriti i due vettori:
1 6 15 20 25
2 20 18 6
Il programma deve visualizzare la sequenza 6 20.
'''
# -----VARIABILI-----
n = 0
n1 = 0
array1 = []
array2 = []
array3 = []
# -------------------
def nIns():
    x = 0
    while(x <= 0):
        print("Inserisci:",end=' ')
        try:
            x = int(input())
            if(x <= 0):
                print("ERRORE. Inserisci un valore intero maggiore di 0")
            elif(x > 30):
                print("ERRORE. Inserisci un valore minore di 30")
                x = 0
        except ValueError:
            print("ERRORE. Inserisci un valore intero maggiore di 0")
    return x

def stamp(vett):
    x = len(vett)
    i = 0
    for i in range(x):
        print(vett[i],end='; ')
    print()

def vettIns(vett,x):
    i = 0
    while(i <= x-1):
        print("Inserisci un valore intero positivo nella posizione",i+1,":",end='')
        elem = int(input())
        vett.append(elem)
        i += 1

def compares(vett1,vett2):
    global array3
    i = j = app = 0
    for i in range(len(vett1)):
        app = vett1[i]
        for j in range(len(vett2)):
            if(vett2[j] == app):
                array3.append(app)

# -----MAIN-----
print("Inserisci la lunghezza del primo Array")
n = nIns()
print("Inserisci la lunghezza del secondo Array")
n1 = nIns()
print("Inserisci",n,"valori all'interno del primo Array")
vettIns(array1,n)
print("Inserisci",n1,"valori all'interno del secondo Array")
vettIns(array2,n1)

print("VALORI INSERITI\nArray1:",end=' ')
stamp(array1)
print("Array2:",end=' ')
stamp(array2)
print("\nIntersezione tra i due vettori:")
compares(array1,array2)
stamp(array3)
