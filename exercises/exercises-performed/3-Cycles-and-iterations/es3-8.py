#Sia dato un numero intero positivo N inserito da tastiera.
#Si scriva un programma in linguaggio Py che calcoli i numeri interi che sono divisori
#(con resto uguale a zero) di N. Dire inoltre se N è un numero primo.
#Suggerimento.
#   • Un numero M è divisore di un numero N se il resto della divisione N/M è uguale a zero.
#   • Un numero è primo se è divisibile solo per 1 o per il numero stesso.

# -----VARIABILI-----

n = 0
i = 1
count = 0

# -------------------


n = int(input("Inserisci un numero N: "))

if n <= 0:
    print("Errore! Hai inserito un numero non valido!!")

print("il numero ",n, "è divisibile per: ")
for i in range(i, n+1):
    if n % i == 0:
        count = count + 1
        print("\t\t\t",i)

if count == 2:
    print("è un numero primo ed è divisibile solo per 1 e per se stesso!!!")




