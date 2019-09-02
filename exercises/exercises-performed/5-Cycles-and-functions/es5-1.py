'''
4.11 Disegno figure geometriche
1. Si realizzi un programma in linguaggio C che legga un numero intero N e visualizzi
    un quadrato di asterischi di lato N (vedi esempio con N = 5).
2. Si realizzi una variante del programma per visualizzare solo i lati del quadrato (vedi esempio con N = 5).
3. Si realizzi una variante del programma per visualizzare un triangolo isoscele rettangolo
    di lato N (vedi esempio con N = 5).
4. Si realizzi una variante del programma per visualizzare un quadrato di lato N come
    nell’esempio del caso 4 (con N = 5).

            Caso 1      Caso 2      Caso 3      Caso 4
            *****       *****       *           *++++
            *****       *   *       **          **+++
            *****       *   *       ***         ***++
            *****       *   *       ****        ****+
            *****       *****       *****       *****
'''

# -----VARIABILI-----

n = 0
asterisco = "*"
piu = "+"
# -------------------



def quadrato (x):
    global asterisco #ho reso globale la variabile per utilizzarla dentro la funzione
    i = 0 # colonna
    j = 0 # riga
    for i in range(x):
        for j in range(x):
            print(asterisco, end='') # print va a capo in automatico, per evitare questo
                                     # utilizzo end per permette di inserire un carattere
                                     # con questo stampo tutta la riga
        print('')

def quadVuoto(x):
    global asterisco
    i=0 #colonna
    j=0 #riga
    for i in range(x):
        for j in range(x):
            if(i==0 or i==x-1 or j==0 or j==x-1):
                print(asterisco, end='')
            elif(j != x-1):
                print(' ', end='')
        print('')

def triangolo(x):
    global asterisco
    # x è il lato del triangolo
    if (x <= 0):
        print('Errore! un trinagolo nonpuò esistere senza lato!')
    else:
        riga = 0
        while(riga < x):
            colonna = 0
            while(colonna <= riga):
                print(asterisco, end='')
                colonna = colonna + 1
            print('')
            riga = riga + 1

def quadTrian(x):
    global asterisco,piu
    if(x <= 0):
        print("Errore! inserire un valore maggiore di 0")
    else:
        riga = 0
        while (riga < x):
            colonna = 0
            while(colonna <= riga):
                print(asterisco, end='')
                colonna = colonna + 1
            while(colonna < x):
                print(piu, end='')
                colonna = colonna + 1
            print('')
            riga = riga + 1



n = int(input("Inserisci un valore per N: "))

print("Caso 1      Caso 2      Caso 3      Caso 4")
print("*****       *****       *           *++++")
print("*****       *   *       **          **+++")
print("*****       *   *       ***         ***++")
print("*****       *   *       ****        ****+")
print("*****       *****       *****       *****")
print('')

s = int(input("Tipo di disegno (1-4):"))
if s == 1:
    quadrato(n)
elif s == 2:
    quadVuoto(n)
elif s == 3:
    triangolo(n)
elif s == 4:
    quadTrian(n)
elif s < 1 or s > 4:
    print("Errore!! Seleziona da 1 a 4")
