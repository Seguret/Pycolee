#Dato un numero intero tra 1 e 12, che rappresenta il mese corrente,
#stampare il nome del mese per esteso (“Gennaio” ... “Dicembre”).

#-----VARIABILI-----

numMese = 0

#-------------------

numMese = int(input("inserisci il numero del mese: "))

options = {
    1 : "Gennaio",
    2 : "Febbraio",
    3 : "Marzo",
    4 : "Aprile",
    5 : "Maggio",
    6 : "Giugno",
    7 : "Luglio",
    8 : "Agosto",
    9 : "Settembre",
    10 : "Ottobre",
    11 : "Novembre",
    12 : "Dicembre"
}

if numMese >= 1 and numMese <= 12:
    print(options[numMese])
else:
    print("non esistono mesi per il numero " + str(numMese))
