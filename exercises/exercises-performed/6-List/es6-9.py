'''Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit
Scrivere un programma che riceve in ingresso un numero binario rappresentato in complemento a 2 su N bit.
Inizialmente l’utente inserisce il numero N di bit.
Quindi inserisce le cifre del numero binario un bit alla volta, partendo dal bit più significativo (MSB).
Terminato l’inserimento del numero, il programma esegue le seguenti operazioni:
1. visualizza il numero inserito partendo dal bit più significativo
2. calcola l’opposto del numero binario ricevuto in ingresso
3. visualizza l’opposto del numero binario ricevuto in ingresso partendo dal bit più significativo (MSB).
Per poter effettuare il calcolo del risultato, utilizzare il metodo secondo
il quale si considerano le cifre del numero binario in complemento a
due, invertite e successivamente sommato 1.

N = 10
Binario Negativo: 1111110011
         Opposto: 0000001100
Binario Positivo: 0000001101
        Decimale: 11

'''
# -----VARIABILI-----
bina = []
n = 0
# -------------------

def nIns():
    x = 0
    while(x <= 0):
        try:
            x = int(input("inserisci il numero N di bit: "))
            if(x <= 0):
                print("ERRORE. Inserisci un numero N di bit intero e positivo")
        except ValueError:
            print("ERRORE. Riprova!")
    return x

def stam(array,x):
    i = 0
    for i in range(x):
        print(array[i], end=' ')

def binarioCom2():
    global n
    n = nIns()
    j = 1
    i = 0
    global bina
    print("inserisce le cifre del numero binario un bit, partendo dal bit più significativo")
    while(i < n):
        try:
            print("Inserisci il bit in posizione",j,":",end='')
            elem = int(input())
            if(elem > 1 or elem < 0):
                print("ERRORE. Valori permessi: 0 e 1")
            else:
                bina.append(elem)
                i += 1
                j += 1
        except ValueError:
            print("ERRORE. Valore non corretto!")
    #print(bina)

    print("\nInserito: ",end='')

    stam(bina,n)
    if(bina[0] == 0):
        print("\n\nUn numero binario negativo non può avere il bit più significativo uguale a 0")
        print("Cambio il bit più significatico uguale a 0 con 1...")
        bina[0] = 1
        print("\nAggiornato: ",end='')
        stam(bina,n)
    #return bina

def binario(array):
    length = len(array)-1
    while(length >= 0):
        if(array[length] == 0):
            array[length] = 1
        elif(array[length] == 1):
            array[length] = 0
        length -= 1
    print("\nOpposto: ",end=' ')
    stam(bina,n)

def somma1(array,x):
    i = x-1
    rest = 1
    while(i >= 0):
        if((array[i]==1 and rest==0) or (array[i]==0 and rest==1)):
            array[i] = 1
            rest = 0
        elif(array[i]==1 and rest==1):
            array[1] = 0
            rest = 1
        else:
            array[i] = 0
            rest = 0
        i -= 1
    print("\nBinario: ",end=' ')
    stam(array,x)

# -----MAIN-----
binarioCom2()
binario(bina)
somma1(bina,n)
