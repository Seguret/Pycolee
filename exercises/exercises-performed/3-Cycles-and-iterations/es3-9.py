#Si scriva un programma in linguaggio Py per calcolare il massimo comun divisore (MCD)
#di due numeri interi positivi. Il MCD è definito come il massimo tra i divisori comuni ai due numeri.
#Suggerimento. Si considerino due numeri interi N1 e N2.
#Il MCD di N1 e N2 è il massimo tra i numeri che sono divisori
#(con resto uguale a zero) sia di N2 che di N1. In particolare,
#si supponga che sia N1 minore di N2. Il MCD è il massimo tra i numeri compresi tra 1 e N1
#che sono divisori (con resto uguale a zero) sia di N1 che di N2.

# -----VARIABILI-----

n1 = 0
n2 = 0
i = 1
mdcN1 = 0
mdcN2 = 0
listN1 = []
listN2 = []
jN1 = 0
jN2 = 0

# -------------------

n1 = int(input("inserisci un numero INTERO per N1: "))
n2 = int(input("inserisci un numero INTERO per N2: "))



if n1 < n2:
    while i < n1:
        if n1 % i == 0 and mdcN1 < i:
            mdcN1 = i
            listN1.insert(jN1, mdcN1)
            jN2 = jN2 + 1
            #print ("resto=",n1 % i, "i =",i)
        if n2 % i == 0 and mdcN2 < i:
            mdcN2 = i
            listN2.insert(jN2, mdcN2)
            jN2 = jN2 + 1
        i = i + 1
    print("Massimo Comune Divisore: ",mdcN1, mdcN2)
else:
    print("N1 deve essere minore di N2")




#print(len(listN2))
