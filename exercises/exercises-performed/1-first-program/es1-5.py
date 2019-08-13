import math

#Si scriva un programma in linguaggio Py che, dato un numero reale D
#immesso da tastiera, calcoli e stampi:
#1. l’area del quadrato di lato D
#2. l’area del cerchio di diametro D
#3. l’area del triangolo equilatero di lato D

#DICHIARAZIONI VARIABILI

d = 0
piGreco = 3.14
quadrato = 0
cerchio = 0
triangoloE = 0

#-----------------------

d = float(input("inserisci un valore reale per D: "))

quadrato = d * d

cerchio = piGreco * d/2 ** 2

triangoloE = (math.sqrt(3) / 4) * d ** 2

print("area di un quadrato di lato D: " + str(quadrato))
print("area di un cerchio di diametro D: " + str(cerchio))
print("area di un triangolo equilatero di lato D: " + str(triangoloE))
