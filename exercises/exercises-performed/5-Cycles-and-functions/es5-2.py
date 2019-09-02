'''Scrivere un programma in linguaggio Py per la rappresentazione del triangolo di Floyd.
Il triangolo di Floyd è un triangolo rettangolo che contiene numeri naturali, definito riempiendo
le righe del triangolo con numeri consecutivi e partendo da 1 nell’angolo in alto a sinistra.
Si consideri ad esempio il caso N=5. Il triangolo di Floyd e’ il seguente:
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
Il programma riceve da tastiera un numero intero N.
Il programma visualizza le prime N righe del triangolo di Floyd.
Suggerimento. Si osserva che il numero di valori in ogni riga corrisponde all’indice della riga: 1 valore sulla prima riga, 2 sulla seconda, 3 sulla terza.'''



def floyd(x):
# -----VARIABILI-----
    i = 0 # riga
    j = 0 # colonna
    count = 1
# -------------------

    for i in range(x): # questo ciclo scandisce le righe
        j = 0
        while(j <= i): # questo ciclo scandisce le colonne
            print(count, end=' ')
            count = count + 1
            j = j + 1
        print('')


n = int(input("Inserisci un valore: "))
floyd(n)
