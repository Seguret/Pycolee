#calcolo del fattoriale di un numero X inserito da tastiera

# -----VARIABILI-----

x = 4
fattoriale = 1

# -------------------

x = int(input("inserisci il valore per cui calcolare il fattoriale: "))

for i in range(1, x + 1):
    #print(i)
    fattoriale = fattoriale * i

print(fattoriale)

