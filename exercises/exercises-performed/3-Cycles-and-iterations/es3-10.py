#Si scriva un programma in linguaggio Py per calcolare il minimo comune multiplo (MCM)
#di due numeri interi positivi. Dati due numeri interi N1 e N2,
#il minimo comune multiplo è il più piccolo numero M che è divisibile
#(con resto pari a zero) sia per N1 che per N2. Suggerimento.
#Si considerino due numeri interi N1 e N2. Sia N1 più grande di N2.
#Il MCM è il primo multiplo di N1 che è divisibile (con resto uguale a zero) per N2.

# -----VARIABILI-----
# tutte le variabili sono inizializzate in anticipo in testa
# questo puo essere un vantaggio per un'eventuale modifica,
# qualora ci si trovasse davanti un listato più corposo si sà dove andare a cercare.
N1 = 0
N2 = 0
massimo = 0
minimo = 0
count = 1
mcm = 0
fine = 0

# -------------------

N1 = int(input("Inserisci un numero per N1: ")) #inserisco il valore per N1
N2 = int(input("Inserisci un numero per N2: ")) #inserisco il valore per N2

if (N1 <= 0 or N2 <= 0):        #Controllo che entrambi i valori siano positivi
    print("Errore: Entrambi i valori devono essere positivi!!!")

if (N1 > N2): #Definisco quale dei due valori inseriti è maggiore e minore
    massimo = N1
    minimo = N2
else:
    minimo = N1
    massimo = N2

while(fine == 0):
    mcm = count * massimo
    if(mcm % minimo == 0):
        fine = 1
    else:
        count = count + 1

print("il minimo comune multiplo di: ", N1, " e ", N2, " è: ", mcm)


