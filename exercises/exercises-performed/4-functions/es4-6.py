#Si scriva un programma in linguaggio Py che acquisisca tre numeri interi da tastiera e:
#   • determini, stampando un messaggio opportuno quale dei tre numeri
#       (il primo, il secondo o il terzo) sia maggiore
#   • stampi il valore di tale numero.
#Si trascuri il caso in cui i numeri siano uguali.

def qualeMggiore(a,b,c):
    if(a > b and a > c):
        print("il maggiore è A: ", a)
    elif b > a and b > c:
        print("Il maggiore è B: ", b)
    elif c > a and c > b:
        print("Il maggiore è C:", c);


qualeMggiore(
    int(
    input("Inserisci A: ")),
    int(
    input("Inserisci B: ")),
    int(
    input("Inserisci C: "))
)
