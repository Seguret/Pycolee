# tabellina di un numero X

# -----VARIABILI-----

x = 1
count = 0
temp = 0

# -------------------

x = int(input("inserisci un valore per X: "))

while (count <= 10):
    temp = x * count
    print("10 *", count, " = ",temp)
    count = count + 1
