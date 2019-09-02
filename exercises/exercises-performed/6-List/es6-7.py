'''
Verificare se un vettore di interi è ordinato
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
I numeri sono memorizzati in un vettore.
Il valore N è inserito dall’utente, ma il vettore può contenere al massimo 30 numeri.
Terminato l’inserimento della sequenza di numeri, il programma deve verificare se il
vettore contiene una sequenza di numeri ordinata in modo strettamente crescente.
'''
def nIns():
    x = 0
    while(x <= 0):
        try:
            x = int(input("Inserisci N: "))
            if(x <= 0):
                print("ERRORE. Inserisci un valore maggiore di 0")
            elif(x > 30):
                print("ERRORE. Inserire un valore minore di 30")
                x = 0
        except ValueError:
            print("ERRORE. Inserire un valore valido")
    return x

def memory():
    n = nIns()
    i = 0
    vett = []
    print("Inserisci",n,"valori nell'array")
    while(i < n):
        try:
            print("Inserisci nella posizione",i,"dell'array:", end='')
            vett.append(int(input()))
            i += 1
        except ValueError:
            print("ERRORE. Valore inserito non corretto")
    return vett

def cresc(vett, ind):
    i = 0
    j = 1
    flag = 0
    print("\n\n-----------------------")
    print("Verifico che gli elementi dell'array siano ordinati in modo crescente...")
    print("Test eseguiti:")
    while(i < ind - 1):
        print(vett[i], "->", vett[j])
        if(vett[i] < vett[j]):
            flag += 1
        else:
            flag = 0
        i += 1
        j += 1
    if(flag == ind - 1):
        print("Gli elementi dell'array sono ordinati in modo cescente")
    else:
        print("Gli elementi dell'array NON sono ordinati")



# -----MAIN-----
array = memory()
print(array)
cresc(array, len(array))
