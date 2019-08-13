#Si realizzi un programma in linguaggio Py per risolvere equazioni di secondo grado.
#In particolare, data una generica equazione di secondo grado nella forma
#               ax2 +bx+c=0
#dove a, b, c sono coefficienti reali noti e x rappresenta l’incognita,
#il programma determini le due radici x1 ed x2 dell’equazione data, ove esse esistano.
#Si identifichino tutti i casi particolari (a = 0, ∆ ≤ 0, ...)
# e si stampino gli opportuni messaggi informativi.

#fare la prova con a=1, b=-3, c=2 risultato x1=2, x2=1

# -----VARIABILI-----

a = 0
b = 0
c = 0

# -------------------
def equa2grado(a, b, c):
    import math
    delta = b*b - 4 * a * c
    if a != 0:
            if delta < 0:
                print("Non ci sono soluzioni in campo reale!")
            elif delta == 0:
                return -b / (2 * a)
            elif delta > 0:
                print("delta= ",delta)
                print("x1= ",(-b + math.sqrt(delta)) / (2 * a))
                print("x2= ",(-b - math.sqrt(delta)) / (2 * a))
    else:
        print("Equazione di secondo grado IMPOSSIBILE!");

print(equa2grado(
    float(input("Inserisci A: ")),
    float(input("Inserisci B: ")),
    float(input("Inserisci C: "))
))

