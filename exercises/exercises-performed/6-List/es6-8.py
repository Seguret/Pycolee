'''Stampa istogrammi
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
Il valore N è inserito dall’utente.
I numeri sono memorizzati in un vettore.
Terminato l’inserimento della sequenza di numeri, il programma deve visualizzare una
riga di asterischi per ogni numero inserito.
Il numero di asterischi nella riga è pari al valore del numero inserito.
Ad esempio, dato il vettore 9 4 6 il programma deve visualizzare:
            Elemento 1: 9 *********
            Elemento 2: 4 ****
            Elemento 3: 6 ******
'''
def nIns():
    x = 0
    while(x <= 0):
        try:
            x = int(input("Inserisci il numero di istogrammi da rappresentare: "))
            if(x <= 0):
                print("ERRORE. Inserisci un valore maggiore di 0")
        except ValueError:
            print("ERRORE. Valore inserito non consentito\nRiprova")
    return x

def memory():
    n = nIns()
    vett = []
    i = 0
    while(i < n):
        try:
            print("Inserisci un valore per la posizione",i,"dell'array: ",end='')
            num = int(input())
            if(num < 0):
                print("ERRORE. Inserisci un numero intero maggiore di 0")
            else:
                vett.append(num)
                i += 1
        except ValueError:
            print("ERRORE. Valore non valido!")
    return vett

def asterisk(vett, ind):
    i = j = 0
    for i in range(ind):
        print("Elemento",i+1,":",vett[i],end=' ')
        k = 0
        j = vett[i]
        while(k < j):
            print("*",end='')
            k += 1
        print()

# -----MAIN-----
array = memory()
asterisk(array, len(array))
