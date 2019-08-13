#calcolo del valore assoluto

def valoreAssoluto (x):
    if x >= 0:
        print(x)
    else:
        print("il valore assoluto è:", abs(x));

valoreAssoluto(int(input("inserisci un valore: ")))
