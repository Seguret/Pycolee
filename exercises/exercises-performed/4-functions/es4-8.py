#Si scriva un programma in linguaggio Py per il calcolo dei quadrati perfetti
#per una sequenza di numeri. Il programma deve prima leggere un numero X inserito da tastiera,
#e quindi stampare i primi quadrati perfetti sino al quadrato del numero.

# -----VARIABILI-----

x = 0
numeroFinale = 0
quadrato = 0

# -------------------

def funQudrato(a, b):
    while a <= b:
        quadrato = a ** 2
        print("Il quadrato di: ",a, "è uguale a: ", quadrato)
        a = a + 1;

x = int(input("Inserisci un numero per X: "))
numeroFinale = int(input("Inserisci un numro per numeroFinale: "))

funQudrato(x, numeroFinale)
