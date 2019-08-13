#Si scriva un programma in linguaggio Py capace di compiere le 4 operazioni
# (somma, sottrazione, moltiplicazione e divisione) tra due numeri reali
# inseriti da tastiera. Dopo che sono stati inseriti i due numeri,
# detti A e B, il programma dovrà visualizzare i quattro valori
# A+B, A-B, A*B, A/B. Si ipotizzi che sia B̸=0.

#DICHIARAZIONE VARIABILI

a = 0
b = 0
ris = 0

#-----------------------

a = float(input("inserisci un numero reale per a: "))
b = float(input("inserisci un numero reale per b: "))

if b != 0:
    ris = a + b
    print("A + B= " + str(ris))

    ris = a - b
    print("A - B= " + str(ris))

    ris = a * b
    print("A * B= " + str(ris))

    ris = a / b
    print("A / B= " + str(ris))
else:
    print("B non può essere uguale a 0")
