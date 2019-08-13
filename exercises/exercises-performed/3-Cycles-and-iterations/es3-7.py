#Si scriva un programma in linguaggio Py per calcolare il valore
#massimo e minimo di un insieme di N numeri inseriti da tastiera.
#Il programma deve leggere il valore di N, ed in seguito deve leggere
#una sequenza di N numeri. A questo punto il programma deve stampare il massimo ed il minimo
#tra i numeri inseriti.

# -----VARIABILI-----

N = 0
massimo = 0
minimo = 0

# -------------------

N = int(input("Quanti elementi vuoi inserire: "))

for i in range(0,N):
    #print("min:", minimo, "max: ", massimo)
    temp = int(input("inserisci un valore: "))
    if  massimo == 0 and minimo == 0:
        massimo = temp
        minimo = temp
    elif temp > massimo and temp < minimo:
        massimo = temp
        minimo = temp
    elif temp > massimo:
        massimo = temp
    elif temp < minimo:
        minimo = temp

print("Minimo: ",minimo)
print("Massimo: ",massimo)


