#Si scriva un programma in linguaggio Py che implementi
#una semplice calcolatrice in grado di
#compiere le 4 operazioni (+ − × ÷) tra numeri interi.
#Il programma presenti un semplice menù da cui l’utente
#indichi (con un numero tra 1 e 4) l’operazione da svolgere.
#In seguito il programma acquisirà da tastiera i due
#operandi e stamperà il risultato dell’operazione.

# -----VARIABILI-----

a = 0
b = 0
c = 0
op = 0

# -------------------

a = int(input("inserisci un valore per a: "))
b = int(input("inserisci un valore per b: "))


print("\n\n•••Menù•••\n1: somma\n2: sottrazione\n3: moltiplicazione\n4: divisione\n")
op = int(input("Scegli: "))
c = {
    1: a + b,
    2: a - b,
    3: a * b,
    4: a / b
}

print(c[op])
