#determinare tutti i numeri pari e dispari di un range da noi specificato

# -----VARIABILI-----

a = 1
b = 6
i = 0

# -------------------

a = int(input("inserisci il numero A: "))
b = int(input("inserisci il numero B: "))

if a < b:
    while (a <= b):
        if a % 2 == 0:
            print("il numero ",a, "è", "pari")
            a = a + 1
        else:
            print("il numero ",a, "è", "dispari")
            a = a + 1
else:
    print("A non può essere più maggiore di B.")

