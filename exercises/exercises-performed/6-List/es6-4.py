'''
Conversione Decimale-Binario su un numero fisso di bit
Scrivere un programma in linguaggio Py che converta un numero decimale D in un
numero binario rappresentato su N bit.
L’utente inserisce un numero decimale intero positivo D e il numero N di bit su cui il
numero decimale deve essere rappresentato.
Il programma visualizzerà i bit che compongono il numero binario partendo dal bit meno significativo.
Il programma segnalerà un errore se il numero N di bit inserito dall’utente non è
sufficiente per rappresentare il numero decimale.

Suggerimento. Per effettuare la conversione usare il metodo delle divisioni successive.
Ad esempio, per convertire il numero decimale D=19 su N=7 bit, si avrà:

Numero      Resto       Cifra binaria       Peso
19          1 (19%2)    1                   0
9 (19/2)    1 (9%2)     1                   1
4 (9/2)     0 (4%2)     0                   2
2 (4/2)     0 (2%2)     0                   3
1 (2/2)     1 (1%2)     1                   4
0 (1/2)     0 (0%2)     0                   5
0 (0/2)     0 (0%2)     0                   6


Nota: nell’applicazione del metodo delle divisioni successive, l’iterazione termina quando
è stato assegnato un valore a ciascuno degli N bit.
'''

# -----VARIABILI-----
D = 0
n = 0
length = 0
i = 0
# -------------------

def conversione(x,y):
    #print(x, " ", y)
    bina=[]
    resto = 0
    j = 0
    l = 0
    length = 0
    while(j <= y-1 and x > 0):
        resto = int(x) % 2
        x = int(x) / 2
        bina.append(resto)
        j = j + 1
    length = len(bina)
    if(x > 0 and j > y-1):
        print("numero N di bit inserito non è sufficiente per rappresentare il numero decimale: ", end='')
        for l in range(length):
            print(bina[l], end=' ')
        print("...")
    else:
        for l in range(length):
            print(bina[l], end=' ')



# -----MAIN-----
while(i == 0): #ciclo sempre vero
    if(D > 0 and n > 0):
        conversione(D, n)
        exit() #per uscire dal programma appena ha concluso la funzione
    else:
        while(D <= 0):
            try:
                D = int(input("Inserisci il numero decimale intero positivo da convertire: "))
            except ValueError:
                print("ERRORE. Inserisci un numero decimale intero positivo")

        while(n <= 0):
            try:
                n = int(input("N di bit su cui il numero decimale deve essere rappresentato: "))
            except ValueError:
                print("ERRORE. Inserisci un numero maggiore di 0")
