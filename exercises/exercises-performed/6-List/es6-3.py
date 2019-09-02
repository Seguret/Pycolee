'''
Somma di numeri binari
Si considerino due numeri binari rappresentati in binario puro su N bit.
Il valore di N viene inserito da tastiera.
I due numeri sono inseriti da tastiera un bit alla volta a partire dal bit meno significativo (LSB).

Si scriva un programma in linguaggio Py per eseguire la somma dei due numeri.
Il programma deve visualizzare il risultato delle somma,
ed indicare se si è verificata la condizione di overflow.
'''


# -----VARIABILI-----
binario1=[]
binario2=[]
n = 0
ris = 0
# -------------------

def nBit():
    x = 0
    while(x <= 0):
        try:
            print("Inserisci il numero di bit: ", end='')
            x = int(input())
            print()
        except ValueError:
            print("ERRORE. Inserire un valore maggiore di 0")
    return x


def inser(bina):
    global n
    i = 0
    while(i < n):
        try:
            print("Insersici il bit in posizione ", i, ": ", end='')
            elem = int(input()[0],2)
            bina.append(elem)
            i = i + 1
        except ValueError:
            print("ERRORE. Valore non corretto!")
    bina.reverse()


def somma(bina1, bina2):
    global n
    i = n-1
    resto = 0
    risultato=[]
    while(i >= 0):
        if((bina1[i] == 0 and bina2[i] == 0 and resto == 1) or (bina1[i] == 0 and bina2[i] == 1 and resto == 0) or (bina1[i] == 1 and bina2[i] == 0 and resto == 0)):
            risultato.append(1)
            resto = 0
        elif((bina1[i] == 0 and bina2[i] == 1 and resto == 1) or (bina1[i] == 1 and bina2[i] == 0 and resto == 1) or (bina1[i] == 1 and bina2[i] == 1 and resto == 0)):
            risultato.append(0)
            resto = 1
        elif(bina1[i] == 1 and bina2[i] == 1 and resto == 1):
            risultato.append(1)
            resto = 1
        elif(bina1[i] == 0 and bina2[i] == 0 and resto == 0):
            risultato.append(0)
            resto = 0
        i = i - 1
    risultato.reverse()
    print("Risultato: ", risultato)
    print("Overflow = ", resto)



# -----MAIN-----
n = nBit() #richiamo la funzione per definire il numero di bit e assegno il risultato a n

#con n definito richiamo la funzione per inserire i bit (0 e 1) nei 2 arrey
print("\nInserisci il 1º numero binario\n------------------------------")
inser(binario1)
print("\nInserisci il 2º numero binario\n------------------------------")
inser(binario2)


print("Binario 1: ",binario1)
print("Binario 2: ",binario2)
somma(binario1, binario2)
