#Si scriva un programma in linguaggio Py che legga
#un valore intero e visualizzi il valore intero precedente e il successivo.

#DICHIARAZIONI VARIABILI

a = 0
b = 0
s = 0

#-----------------------

a = int(input("inserisci un valore per a: "))
b = a-1
s = a+1
print(str(b) + " " + str(a) + " " + str(s))
