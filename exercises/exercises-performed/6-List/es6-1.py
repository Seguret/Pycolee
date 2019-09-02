'''Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit

Scrivere un programma in linguaggio Py che riceva in ingresso un numero binario rappresentato
 in complemento a 2 su N bit.
 Inizialmente l’utente inserisce il numero N di bit.
 Quindi inserisce le cifre del numero binario un bit alla volta, partendo dal bit meno significativo (IL BIT PIU' A SX).

 Il programma calcola l’opposto del numero binario ricevuto in ingresso.

Suggerimento. Per poter effettuare il calcolo del risultato, utilizzare il metodo secondo il quale,
partendo dal complemento a 1, si somma 1 dal bit meno significativo al bit più significativo,
considerando tutti i resti ad eccezione dell'eventuale resto prodotto dal bit più significativo.

      35 -> Decimale
00100011 -> Binario Positivo
11011100 -> Opposto
11011101 -> Binario Negativo (Complemento a 2)

      12 -> Decimale
00001100 -> Binario Positivo
11110011 -> Opposto
11110100 -> Binario Negativo (Complemento a 2)
'''
# -----VARIABILI-----
N = 0
x = 0
binario=[]
# -------------------
def complemento(x):
    i = 0
    resto = 1
    global binario
    while(i < x): #complemento a 1
        if(binario[i]==0):
            binario[i] = 1
        else:
            binario[i]=0
        i = i + 1

    print(binario,"Complemento a 1")

    i = x-1
    while(i > 0):
        if(binario[i]==1 and resto==1):
            #resto = 1
            binario[i]=0
        elif(binario[i]==0 and resto==1):
            binario[i]=1
            resto=0
        i = i - 1
    print(binario, "Complemento a 2")



while(N <= 0):
    if(x > 0):
        print("ERRORE!! Il numero di bit deve essere > di 0")
    N = int(input("inserisci il numero di bit: "))
    x = x + 1

print("Inserisci i bit dal meno significativo(IL BIT PIU' A DESTRA)")
i = N-1
while(i >= 0):
    print("inserisci il bit di posizione", i, ": ")
    bit = int(input())
    binario.append(bit) #utilizzo append e NO insert perchè append inserisce in
                        # fondo alla lista mentre insert durante l'iserimento
                        # ordina i valore in modo crescen
    i = i - 1
binario.reverse()
complemento(N)
