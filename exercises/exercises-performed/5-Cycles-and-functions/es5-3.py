'''Numeri di Fibonacci
Scrivere un programma in linguaggio Py che calcoli e stampi i primi N numeri
della serie di Fibonacci, con N inserito da tastiera.

La serie di Fibonacci inizia con 1, 1 ed ogni numero successivo è dato dalla
somma dei due precedenti: 1, 1, 2, 3, 5, 8, 13, 21 . . .
'''
# -----VARIABILI-----
n = 0
# -------------------
def nIns():
    x = 0
    while(x <= 0):
        try:
            x = int(input("Inserisci un valore per N: "))
            if(x <= 0):
                print("ERRORE. Inserire un valore per N maggiore di 0")
        except ValueError:
            print("ERRORE. Campo numerico!\nInserire un valore positivo intero")
    return x

def bonacci(x):
    a = p = 1
    i = 0
    r = 0
    print(a ,p, end=' ')
    for i in range(x):
        r = a + p
        print(r, end=' ')
        p = a
        a = r
        i = i + 1

# -----MAIN-----

n = nIns()
bonacci(n)

