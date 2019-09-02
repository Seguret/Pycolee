# **Esercizi di Programmazione in Python**
Esercitazioni per il progetto **Pycolee**


## **INDICE**

### **1 Primo programma in Py**
- 1.1 Somma di due numeri
- 1.2 Precedente e Successivo
- 1.3 Media tra due numeri
- 1.4 Semplice calcolatrice
- 1.5 calcolo di aree

### **2 Scelte ed alternative**
- 2.1 Segno del numero
- 2.2 Controlla A e B
- 2.3 Classificazione triangolo
- 2.4 Equazione di primo grado
- 2.5 Stampa dei mesi
- 2.6 Semplice calcolatrice
- 2.7 Calcolo del massimo

### **3 Cicli ed iterazioni**
- 3.1 Somma tutti i numeri di una lista
- 3.2 Tabellina di un numero X
- 3.3 Stampare le lettere di una stringa (Versione avanzata)
- 3.4 Fattoriale
- 3.5 Range di numeri
- 3.6 Media dei numeri
- 3.7 Massimo e minimo
- 3.8 Divisori di un numero
- 3.9 Massimo comune divisore tra 2 numeri
- 3.10 Minimo comune multiplo tra 2 numeri


### **4 Funzioni**
- 4.1 Moltiplicazione
- 4.2 Anagrafica
- 4.3 Dentro e fuori dalla funzione
- 4.5 Valore Assoluto
- 4.6 Potenza di N
- 4.7 Calcolo del massimo
- 4.8 Calcolo del massimo a 3
- 4.9 Quadrati perfetti

### **5 Cicli e funzioni**
- 5.1 Disegno figure geometriche
- 5.2 Rappresentazione del triangolo di Floyd
- 5.3 Numeri di Fibonacci

###**6 Liste**
- 6.1 Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit
- 6.2 Conversione Binario-Decimale
- 6.3 Somma di numeri binari
- 6.4 Conversione Decimale-Binario su un numero fisso di bit
- 6.5 Ricerca di un elemento in vettore
- 6.6 Verificare se un vettore contiene tutti elementi tra loro uguali
- 6.7 erificare se un vettore di interi è ordinato
- 6.8 Stampa istogrammi
- 6.9 Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit
- 6.10 Operazione di shift di un vettore
- 6.11 Compattazione di un vettore
- 6.12 Intersezione di due vettori






--
_Capitolo **1**_
# **Primo programma in Py**
--
#### 1.1 Somma di due numeri
Si scriva un programma in linguaggio Py che legga due valori interi e visualizzi la loro somma
#### Soluzione

	import math

	#DICHIARAZIONI VARIABILI

	a = 0
	b = 0
	s = 0

	#-----------------------
	
	a = int(input("inserisci un valore per a: "))
	b = int(input("inserisci un valore per b: "))
	
	s = a + b
	
	print(s)
	
--
####1.2 Precedente e Successivo
Si scriva un programma in linguaggio Py che legga un valore intero e visualizzi il valore intero precedente e il successivo.
####Soluzione
	#DICHIARAZIONI VARIABILI

	a = 0
	b = 0
	s = 0
	
	#-----------------------
	
	a = int(input("inserisci un valore per a: "))
	b = a-1
	s = a+1
	print(str(b) + " " + str(a) + " " + str(s))
--

####1.3 Media tra due numeri
Si scriva un programma in linguaggio Py che legga due valori interi e visualizzi la loro media aritmetica.
####Soluzione
	#DICHIARAZIONI VARIABILI

	a = 0
	b = 0
	media = 0
	
	#-----------------------
	
	a = int(input("inserisci un intero per a: "))
	b = int(input("inserisci un intero per b: "))
	
	media = (a + b) / 2
	
	print(media)
--
####1.4 Semplice calcolatrice
Si scriva un programma in linguaggio Py capace di compiere le 4 operazioni (somma, sottrazione, moltiplicazione e divisione) tra due numeri reali inseriti da tastiera. Dopo che sono stati inseriti i due numeri, detti A e B, il programma dovrà visualizzare i quattro valori A+B, A-B, A*B, A/B. Si ipotizzi che sia B̸=0.
####Soluzione
	#DICHIARAZIONE VARIABILI
	
	a = 0
	b = 0
	ris = 0
	
	#-----------------------
	
	a = float(input("inserisci un numero reale per a: "))
	b = float(input("inserisci un numero reale per b: "))
	
	if b != 0:
	    ris = a + b
	    print("A + B= " + str(ris))
	
	    ris = a - b
	    print("A - B= " + str(ris))
	
	    ris = a * b
	    print("A * B= " + str(ris))
	
	    ris = a / b
	    print("A / B= " + str(ris))
	else:
	    print("B non può essere uguale a 0")
--
####1.5 calcolo di aree
Si scriva un programma in linguaggio Py che, dato un numero reale D immesso da tastiera, calcoli e stampi:

1. l’area del quadrato di lato D
2. l’area del cerchio di diametro D
3. l’area del triangolo equilatero di lato D

####Soluzione
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


--
_Capitolo **2**_
# **Scelte ed alternative**
--
####2.1 Indovina cosa...
Si realizzi un programma in linguaggio Py che acquisisca da tastiera un numero e stampi un messaggio che indichi se tale numero sia positivo oppure negativo e stampi il valore assoluto di tale numero.
####Soluzione
	import math
	
	#DICHIARAZIONE VARIABILI
	
	x = 0
	
	#-----------------------
	
	x = float(input("inserisci un valore X: "))
	
	if x > 0:
	    print("Il valore è positivo")
	elif x == 0:
	    print("il valore è uguale a 0")
	else:
	    print("il valore è negativo")
	    x = abs(x)
	    print("il valore assoluto di X è: " + str(x))
	    
--
####2.2 Controlla A e B
Si scriva un programma in linguaggio Py che legga due numeri da tastiera, detti A e B, e determini le seguenti informazioni, stampandole a video:

1. determini se B è un numero positivo o negativo
2. determini se A è un numero pari o dispari
3. calcoli il valore di A + B
4. determini quale scelta dei segni nell’espressione (±A) + (±B) porta al risultato mas- simo, e quale è questo valore massimo.

Suggerimento. Nel punto 4., il valore massimo della somma di A e B si può ottenere sommando il valore assoluto di A e di B.

####Soluzione
	#DICHIARAZIONE VARIABILI
	
	a = 0
	b = 0
	c = 0
	
	#-----------------------
	
	a = float(input("inserisci un numero per A: "))
	b = float(input("inserisci un numero per B: "))
	
	if b > 0:
	    print("B è positivo!")
	elif b < 0:
	    print("B è negativo!")
	else:
	    print("B è uguale a 0!")
	
	if (a % 2) == 0:
	    print("A è un numero pari!")
	else:
	    print("A è un numero dispari!")
	
	
	
	print("la somma tra A e B è: " + str(a + b))
	
	if a < 0:
	    a = abs(a)
	
	if b < 0:
	    b = abs(b)
	
	print("il valore massimo della somma +-A + +-B è uguale a: " + str(a+b))
--
####2.3 Classificazione triangolo
Si scriva un programma in linguaggio Py che legga da tastiera i valori delle lunghezze dei tre lati di un triangolo (detti A, B e C), e determini:

- se il triangolo è equilatero  
- se il triangolo è isoscele
- se il triangolo è scaleno
- se il triangolo è rettangolo.

####Soluzione
	#----VARIABILI----
	
	a = 0
	b = 0
	c = 0
	
	#-----------------
	
	a = float(input("inserisci il lato A: "))
	b = float(input("inserisci il lato B: "))
	c = float(input("inserisci il lato C: "))
	
	if a == b == c:
	    print("Equilatero!")
	elif a==b or b==c or a==c:
	    print("Isoscele!")
	elif a!=b and b!=c and a!=c:
	    print("Scaleno!")
	
	if a*a == b*b + c*c:
	    print("Il triangolo è rettangolo!")
	else:
	    print("Il triangolo non è rettangolo!")
	    
--
####2.4 Equazione di primo grado
Data l’equazione
>ax + b = 0

con a e b inseriti da tastiera, scrivere un programma in linguaggio Py
per determinare il valore di x, se esiste, che risolve l’equazione.

NOTA: x viene calcolata come x = -b/a
####Soluzione
	#-----VARIABILI-----
	
	a = 0
	b = 0
	x = 0
	
	#-------------------
	
	a = float(input("inserisci a: "))
	b = float(input("inserisci b: "))
	
	if a != 0:
	    x = -b / a
	    print("la soluzione è: ", str(x))
	else:
	    if b == 0:
	        print("Equazione indeterminata (ammette infinite soluzioni)")
	    else:
	        print("Equazione Impossibile (non ammette soluzioni)")
--
####2.5 Stampa dei mesi
Dato un numero intero tra 1 e 12, che rappresenta il mese corrente,
stampare il nome del mese per esteso (“Gennaio” ... “Dicembre”).
####Soluzione
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
--
####2.6 Semplice calcolatrice
Si scriva un programma in linguaggio Py che implementi
una semplice calcolatrice in grado di
compiere le 4 operazioni (+ − × ÷) tra numeri interi.
Il programma presenti un semplice menù da cui l’utente
indichi (con un numero tra 1 e 4) l’operazione da svolgere.
####Soluzione
	# -----VARIABILI-----
	
	a = 0
	b = 0
	c = 0
	op = 0
	
	# -------------------
	
	a = int(input("inserisci un valore per a: "))
	b = int(input("inserisci un valore per b: "))
	
	
	print("\n\n•••Menù•••\n1: somma\n2: sottrazione\n3: moltiplicazione\n4: divisione\n")
	op = int(input("Scegli: "))
	c = {
	    1: a + b,
	    2: a - b,
	    3: a * b,
	    4: a / b
	}
	
	print(c[op])
--
####2.7 Calcolo del massimo
Si scriva un programma in linguaggio Py che acquisisca due numeri interi da tastiera e: 

- determini, stampando un messaggio opportuno quale dei due numeri (il primo o il secondo) sia maggiore
-  stampi il valore di tale numero.

####Soluzione
	# -----VARIABILI-----
	
	a = 0
	b = 0
	
	# -------------------
	
	a = int(input("inserisci un valore per A: "))
	b = int(input("inserisci un valore per B: "))
	
	if a > b:
	    print("\nIl maggiore è: ", a)
	else:
	    print("\nIl maggiore è: ", b)
	
--
_Capitolo **3**_
# **Cicli ed iterazioni**
--
#### 3.1 Somma tutti i numeri contenuti in una lista

####Soluzione
	# -----VARIABILI-----
	
	numeri = [10,20,30,40,50]
	somma = 0
	
	# -------------------
	
	for x in numeri:
	    somma = somma + x
	
	print(somma)
	
--
####3.2 Calcola la tabellina di un numero X

####Soluzione
	# -----VARIABILI-----
	
	x = 1
	count = 0
	temp = 0
	
	# -------------------
	
	x = int(input("inserisci un valore per X: "))
	
	while (count <= 10):
	    temp = x * count
	    print("10 *", count, " = ",temp)
	    count = count + 1
	    
--
####3.3 Stampare le lettere di una stringa (Versione avanzata)
stampare le lettere di una stringa una ad una. 
stampare il messaggio: la lettera X è "lettera" con la lettera di un altro colore
####Soluzione
	# -----VARIABILI-----
	
	text = ""
	counter = 1
	class bcolors:
	    HEADER = '\033[95m' #rosa
	    OKBLUE = '\033[94m' #celeste
	    OKGREEN = '\033[92m' #verde acido
	    WARNING = '\033[93m' #giallo
	    FAIL = '\033[91m' #salmone
	    ENDC = '\033[0m' # bianco
	    BOLD = '\033[1m' #grassetto
	    UNDERLINE = '\033[4m' #sottolineato
	
	# -------------------
	
	text = input("inserisci una stringa: ")
	
	for i in text:
	    print ( bcolors.ENDC +  "la lettera ",counter, "è",(bcolors.FAIL + bcolors.BOLD + i))
	    counter = counter + 1
	    
--
#### 3.4 Fattoriale

Si scriva un programma in linguaggio Py che acquisisca un numero intero positivo N da tastiera e stampi il valore del fattoriale di N.

Suggerimento. Si ricorda che il fattoriale di un numero è il prodotto di tutti i numeri compresi tra 1 ed N.
#### Soluzione
	# -----VARIABILI-----
	
	x = 4
	fattoriale = 1
	
	# -------------------
	
	x = int(input("inserisci il valore per cui calcolare il fattoriale: "))
	
	for i in range(1, x + 1):
	    #print(i)
	    fattoriale = fattoriale * i
	
	print(fattoriale)
--
####3.5 Range di numeri
 determinare tutti i numeri pari e dispari di un range da noi specificato
####Soluzione
	# -----VARIABILI-----
	
	a = 1
	b = 6
	i = 0
	
	# -------------------
	
	a = int(input("inserisci il numero A: "))
	b = int(input("inserisci il numero B: "))
	
	if a < b:
	    while (a <= b):
	        if a % 2 == 0:
	            print("il numero ",a, "è", "pari")
	            a = a + 1
	        else:
	            print("il numero ",a, "è", "dispari")
	            a = a + 1
	else:
	    print("A non può essere più maggiore di B.")
--
####3.6 Media dei numeri
Si scriva un programma in linguaggio Py per calcolare la media aritmetica di una serie di
numeri inseriti da tastiera. L’introduzione tramite il valore "exit"
indica il termine del caricamento dei dati.
####Soluzione
	# -----VARIABILI-----
	
	somma = 0
	x = 0
	count = 0
	
	# -------------------
	
	while x != "exit":
	    x = input("inserisci valore: ")
	    if x != "exit":
	        somma = somma + int(x)
	        count = count + 1
	
	
	print(somma/count)
--
####3.7 Massimo e minimo
Si scriva un programma in linguaggio Py per calcolare il valore
massimo e minimo di un insieme di N numeri inseriti da tastiera.
Il programma deve leggere il valore di N, ed in seguito deve leggere
una sequenza di N numeri. A questo punto il programma deve stampare il massimo ed il minimo
tra i numeri inseriti.
####Soluzione
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
--
####3.8 Divisori di un numero
Sia dato un numero intero positivo N inserito da tastiera.
Si scriva un programma in linguaggio Py che calcoli i numeri interi che sono divisori
(con resto uguale a zero) di N. Dire inoltre se N è un numero primo.

Suggerimento:

- Un numero M è divisore di un numero N se il resto della divisione N/M è uguale a zero.
- Un numero è primo se è divisibile solo per 1 o per il numero stesso.

####Soluzione
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
--
####3.9 Massimo comune divisore tra 2 numeri
scriva un programma in linguaggio Py per calcolare il massimo comun divisore (MCD)
di due numeri interi positivi. Il MCD è definito come il massimo tra i divisori comuni ai due numeri.

Suggerimento. Si considerino due numeri interi N1 e N2.
Il MCD di N1 e N2 è il massimo tra i numeri che sono divisori
(con resto uguale a zero) sia di N2 che di N1. In particolare,
si supponga che sia N1 minore di N2. Il MCD è il massimo tra i numeri compresi tra 1 e N1
che sono divisori (con resto uguale a zero) sia di N1 che di N2.
####Soluzione
	# -----VARIABILI-----
	
	n1 = 0
	n2 = 0
	i = 1
	mdcN1 = 0
	mdcN2 = 0
	listN1 = []
	listN2 = []
	jN1 = 0
	jN2 = 0
	
	# -------------------
	
	n1 = int(input("inserisci un numero INTERO per N1: "))
	n2 = int(input("inserisci un numero INTERO per N2: "))
	
	
	
	if n1 < n2:
	    while i < n1:
	        if n1 % i == 0 and mdcN1 < i:
	            mdcN1 = i
	            listN1.insert(jN1, mdcN1)
	            jN2 = jN2 + 1
	            #print ("resto=",n1 % i, "i =",i)
	        if n2 % i == 0 and mdcN2 < i:
	            mdcN2 = i
	            listN2.insert(jN2, mdcN2)
	            jN2 = jN2 + 1
	        i = i + 1
	    print("Massimo Comune Divisore: ",mdcN1, mdcN2)
	else:
	    print("N1 deve essere minore di N2")
--
####3.10 Minimo comune multiplo tra 2 numeri
Si scriva un programma in linguaggio Py per calcolare il minimo comune multiplo (MCM)
di due numeri interi positivi. Dati due numeri interi N1 e N2,
il minimo comune multiplo è il più piccolo numero M che è divisibile
(con resto pari a zero) sia per N1 che per N2. 

Suggerimento.
Si considerino due numeri interi N1 e N2. Sia N1 più grande di N2.
Il MCM è il primo multiplo di N1 che è divisibile (con resto uguale a zero) per N2.

Prova: con i numeri 18 e 27 il mcm è 54
####Soluzione
	# -----VARIABILI-----
	# tutte le variabili sono inizializzate in anticipo in testa
	# questo puo essere un vantaggio per un'eventuale modifica,
	# qualora ci si trovasse davanti un listato più corposo si sà dove andare a cercare.
	N1 = 0
	N2 = 0
	massimo = 0
	minimo = 0
	count = 1
	mcm = 0
	fine = 0
	
	# -------------------
	
	N1 = int(input("Inserisci un numero per N1: ")) #inserisco il valore per N1
	N2 = int(input("Inserisci un numero per N2: ")) #inserisco il valore per N2
	
	if (N1 <= 0 or N2 <= 0):        #Controllo che entrambi i valori siano positivi
	    print("Errore: Entrambi i valori devono essere positivi!!!")
	
	if (N1 > N2): #Definisco quale dei due valori inseriti è maggiore e minore
	    massimo = N1
	    minimo = N2
	else:
	    minimo = N1
	    massimo = N2
	
	while(fine == 0):
	    mcm = count * massimo
	    if(mcm % minimo == 0):
	        fine = 1
	    else:
	        count = count + 1
	
	print("il minimo comune multiplo di: ", N1, " e ", N2, " è: ", mcm)



--
_Capitolo **4**_
# **Funzioni**
--
#### 4.1 Moltiplicazione
Moltiplica un numero per una costante
####Soluzione
	def molti(moltiplicando):
	    x = 5
	    return x * moltiplicando
	
	m = int(input("quale numero vuoi moltiplicare per 5? "))
	
	print(molti(m))
--
####4.2 Anagrafica
stampa informazioni di un utente inserite da tastiera
####Soluzione

	def user(n, c, e, em):
	    print("Nome:" , n)
	    print("Cognome:" , c)
	    if e != "":
	        print("età:" , e)
	    else:
	        print("età: 18")
	    print("E-mail:" , em)
	
	
	nome = input("Inserisci il nome: ")
	cognome = input("Inserisci il cognome: ")
	eta = input("Inserisci l'età: ")
	email = input("Inserisci la mail: ")
	
	print("\n\n")
	user(nome,cognome,eta,email)
--
####4.3 Dentro e fuori dalla funzione
stampa dentro e fuori la funzione la somma di 2 numeri
####Soluzione

	# -----VARIABILI-----
	
	
	# -------------------
	
	def addizione(a, b): #arg1 e arg2
	    somma = a + b
	    print("stampa dentro la funzione: ", somma)
	    return somma;
	
	totaleFuori = addizione(10,20)
	print("stampa fuori la funzione: ", totaleFuori)
	
--
####4.4 Valore assoluto
calcola il valore assoluto di un numero inserito da tastiera
####Soluzione
	def valoreAssoluto (x):
	    if x >= 0:
	        print(x)
	    else:
	        print("il valore assoluto è:", abs(x));
	
	valoreAssoluto(int(input("inserisci un valore: ")))
--
####4.5 Potenza di N
calcola l'elevazione a potenza di un numero dopo che sia la base che l'esponenete siano stati inseriti da tastiera.
Suggerimento: l'elevazione a potenza è la base moltiplicata per se stessa tante volte quante indicate dall'esponente (es. 3^2 = 3*3; 5^4 = 5\*5\*5\*5)
####Soluzione
	def potenza(x, y):
	    return x**y;
	
	print(potenza(
	        int(input("inserisci base:")),
	        int(input("inserisci esponente:"))
	            )
	     )
--
####4.6 Calcolo del massimo a 3
Si scriva un programma in linguaggio Py che acquisisca tre numeri interi da tastiera e:

- determini, stampando un messaggio opportuno quale dei tre numeri
       (il primo, il secondo o il terzo) sia maggiore
- stampi il valore di tale numero.

Si trascuri il caso in cui i numeri siano uguali.

####soluzione
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

--
####4.7 Equazione di secondo grado

Si realizzi un programma in linguaggio Py per risolvere equazioni di secondo grado.
In particolare, data una generica equazione di secondo grado nella forma
>ax2 +bx+c=0

dove a, b, c sono coefficienti reali noti e x rappresenta l’incognita,
il programma determini le due radici x1 ed x2 dell’equazione data, ove esse esistano.

Si identifichino tutti i casi particolari (a = 0, ∆ ≤ 0, ...)
 e si stampino gli opportuni messaggi informativi.

fare la prova con a=1, b=-3, c=2 risultato x1=2, x2=1
####Soluzione
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
--
####4.8 Quadrati perfetti
Si scriva un programma in linguaggio Py per il calcolo dei quadrati perfetti
per una sequenza di numeri. Il programma deve prima leggere un numero X inserito da tastiera,
e quindi stampare i primi quadrati perfetti sino al quadrato del numero.
####Soluzione
	# -----VARIABILI-----
	
	x = 0
	numeroFinale = 0
	quadrato = 0
	
	# -------------------
	
	def funQudrato(a, b):
	    while a <= b:
	        quadrato = a ** 2
	        print("Il quadrato di: ",a, "è uguale a: ", quadrato)
	        a = a + 1;
	
	x = int(input("Inserisci un numero per X: "))
	numeroFinale = int(input("Inserisci un numro per numeroFinale: "))
	
	funQudrato(x, numeroFinale)
--
####4.9 Fattoriale
Si scriva un programma in linguaggio Py che acquisisca un numero intero positivo N da tastiera
e stampi il valore del fattoriale di N.

Suggerimento. Si ricorda che il fattoriale di un numero è il prodotto di
tutti i numeri compresi tra 1 ed N.
####Soluzione
	# -----VARIABILI-----
	
	n = 0
	
	# -------------------
	
	def fattoriale(x):
	    i = 1
	    j = x
	    while i < j:
	        x = x * i
	        i = i + 1
	    print(x)
	
	
	n = int(input("Inserisci un valore per N: "))
	
	fattoriale(n)
--
_Capitolo **5**_
# **Cicli e funzioni**
--
####5.1 Disegno figure geometriche

1. Si realizzi un programma in linguaggio Py che legga un numero intero N e visualizzi
    un quadrato di asterischi di lato N.
    
2. Si realizzi una variante del programma per visualizzare solo i lati del quadrato.

3. Si realizzi una variante del programma per visualizzare un triangolo isoscele rettangolo
    di lato N.
    
4. Si realizzi una variante del programma per visualizzare un quadrato di lato N come
    nell’esempio del caso 4.
    
Esempio con N = 5

            Caso 1      Caso 2      Caso 3      Caso 4
            *****       *****       *           *++++
            *****       *   *       **          **+++
            *****       *   *       ***         ***++
            *****       *   *       ****        ****+
            *****       *****       *****       *****
 
####Soluzione

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

	    
####Nota
Proporre le 4 soluzioni con 2 cicli diversi (for e while) è solo dimostrativo e non deve essere limitante, anzi deve essere di stimolo per ricercare altre soluzioni.

--
####5.2 Rappresentazione del triangolo di Floyd
Scrivere un programma in linguaggio Py per la rappresentazione del triangolo di Floyd.
Il triangolo di Floyd è un triangolo rettangolo che contiene numeri naturali, definito riempiendo
le righe del triangolo con numeri consecutivi e partendo da 1 nell’angolo in alto a sinistra.
Si consideri ad esempio il caso N=5. Il triangolo di Floyd e’ il seguente:

        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
Il programma riceve da tastiera un numero intero N.
Il programma visualizza le prime N righe del triangolo di Floyd.

Suggerimento. 
Si osserva che il numero di valori in ogni riga corrisponde all’indice della riga: 1 valore sulla prima riga, 2 sulla seconda, 3 sulla terza.


####Soluzione
	def floyd(x):
	# -----VARIABILI-----
	    i = 0 # riga
	    j = 0 # colonna
	    count = 1
	# -------------------
	
	    for i in range(x): # questo ciclo scandisce le righe
	        j = 0
	        while(j <= i): # questo ciclo scandisce le colonne
	            print(count, end=' ')
	            count = count + 1
	            j = j + 1
	        print('')
	
	
	n = int(input("Inserisci un valore: "))
	floyd(n)

--
####5.3 Numeri di Fibonacci
Scrivere un programma in linguaggio Py che calcoli e stampi i primi N numeri
della serie di Fibonacci, con N inserito da tastiera.

La serie di Fibonacci inizia con 1, 1 ed ogni numero successivo è dato dalla
somma dei due precedenti: 1, 1, 2, 3, 5, 8, 13, 21 . . .
####Soluzione
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


--
_Capitolo **6**_
# **Liste**
--
####6.1 Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit
Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit

Scrivere un programma in linguaggio Py che riceva in ingresso un numero binario rappresentato
 in complemento a 2 su N bit.
 Inizialmente l’utente inserisce il numero N di bit.
 Quindi inserisce le cifre del numero binario un bit alla volta, partendo dal bit meno significativo (IL BIT PIU' A SINISTRA).

 Il programma calcola l’opposto del numero binario ricevuto in ingresso.


	      35 -> Decimale
	00100011 -> Binario Positivo
	11011100 -> Opposto
	11011101 -> Binario Negativo (Complemento a 2)
	
	      12 -> Decimale
	00001100 -> Binario Positivo
	11110011 -> Opposto
	11110100 -> Binario Negativo (Complemento a 2)
Suggerimento. Per poter effettuare il calcolo del risultato, utilizzare il metodo secondo il quale,
partendo dal complemento a 1, si somma 1 dal bit meno significativo al bit più significativo,
considerando tutti i resti ad eccezione dell'eventuale resto prodotto dal bit più significativo.
####Soluzione
	# -----VARIABILI-----
	N = 0
	x = 0
	binario=[]
	# -------------------
	def complemento(x):
	    i = 0
	    resto = 1
	    global binario
	    while(i < x): #complemento a 1
	        if(binario[i]==0):
	            binario[i] = 1
	        else:
	            binario[i]=0
	        i = i + 1
	
	    print(binario,"Complemento a 1")
	
	    i = x-1
	    while(i > 0):
	        if(binario[i]==1 and resto==1):
	            #resto = 1
	            binario[i]=0
	        elif(binario[i]==0 and resto==1):
	            binario[i]=1
	            resto=0
	        i = i - 1
	    print(binario, "Complemento a 2")
	
	
	
	while(N <= 0):
	    if(x > 0):
	        print("ERRORE!! Il numero di bit deve essere > di 0")
	    N = int(input("inserisci il numero di bit: "))
	    x = x + 1
	
	print("Inserisci i bit dal meno significativo(IL BIT PIU' A DESTRA)")
	i = N-1
	while(i >= 0):
	    print("inserisci il bit di posizione", i, ": ")
	    bit = int(input())
	    binario.append(bit) #utilizzo append e NO insert perchè append inserisce in
	                        # fondo alla lista mentre insert durante l'iserimento
	                        # ordina i valore in modo crescen
	    i = i - 1
	binario.reverse()
	complemento(N)
--
####6.2 Conversione Binario-Decimale
Si scriva un programma in linguaggio Py che converta un numero binario in un numero decimale.
Il numero binario è rappresentato su N bit, e il valore di N è inserito da tastiera.
L’utente inserisce le cifre del numero binario un bit alla volta, partendo dal bit meno significativo
(ossia dal bit di peso 20).
Il programma visualizzerà il numero decimale corrispondente.
Gestire tutti gli errori di inserimento.

Suggerimento. Per calcolare le potenze di 2 utilizzare la funzione pow, includendo la libreria math.h.
Ad esempio per calcolare 25, si scriverà pow(2,5). In generale, data una base a, per calcolare y = ab,
si scrive y = pow(a,b) includendo la libreria math.h.
####Soluzione

	import math
	# -----VARIABILI-----
	lista=[]
	i = 0
	bit = 0
	n = 0
	# -------------------
	
	def inser(bina, elem):
	    bina.append(elem)
	
	def conversione(bina):
	    global n
	    decimale = 0
	    expo = 0
	    j = n - 1
	    while(j >= 0):
	        if(bina[j]==1):
	            decimale = decimale + (bina[j]*pow(2,expo))
	        expo = expo + 1
	        j = j - 1
	    print(bina)
	    print(decimale)
	
	# -----MAIN-----
	while(n <= 0):
	    try: #il try è stato inserito per gestire gli errori di inserimento (es. stringhe, null)
	        n = int(input("Inserisce il numero di bit: "))
	        if(n <= 0):
	            print("ERRORE. Inserire un valore > di 0")
	    except ValueError:
	        print("ERRORE. \n Riprova")
	
	while(i < n):
	    try:
	        print("inserisci il bit num ", i, ": ")
	        bit = int(input(),2)
	        inser(lista, bit)
	        i = i + 1
	    except ValueError: #mentre questo try è per gestire tutti i valori inseriti diversi da 0 e 1
	        print("ERRORE.")
	
	lista.reverse()
	conversione(lista)
--
####6.3 Somma di numeri binari
Si considerino due numeri binari rappresentati in binario puro su N bit.
Il valore di N viene inserito da tastiera.
I due numeri sono inseriti da tastiera un bit alla volta a partire dal bit meno significativo (LSB).

Si scriva un programma in linguaggio Py per eseguire la somma dei due numeri.
Il programma deve visualizzare il risultato delle somma,
ed indicare se si è verificata la condizione di overflow.
####Soluzione

	# -----VARIABILI-----
	binario1=[]
	binario2=[]
	n = 0
	ris = 0
	# -------------------
	
	def nBit():
	    x = 0
	    while(x <= 0):
	        try:
	            print("Inserisci il numero di bit: ", end='')
	            x = int(input())
	            print()
	        except ValueError:
	            print("ERRORE. Inserire un valore maggiore di 0")
	    return x
	
	
	def inser(bina):
	    global n
	    i = 0
	    while(i < n):
	        try:
	            print("Insersici il bit in posizione ", i, ": ", end='')
	            elem = int(input()[0],2)
	            bina.append(elem)
	            i = i + 1
	        except ValueError:
	            print("ERRORE. Valore non corretto!")
	    bina.reverse()
	
	
	def somma(bina1, bina2):
	    global n
	    i = n-1
	    resto = 0
	    risultato=[]
	    while(i >= 0):
	        if((bina1[i] == 0 and bina2[i] == 0 and resto == 1) or (bina1[i] == 0 and bina2[i] == 1 and resto == 0) or (bina1[i] == 1 and bina2[i] == 0 and resto == 0)):
	            risultato.append(1)
	            resto = 0
	        elif((bina1[i] == 0 and bina2[i] == 1 and resto == 1) or (bina1[i] == 1 and bina2[i] == 0 and resto == 1) or (bina1[i] == 1 and bina2[i] == 1 and resto == 0)):
	            risultato.append(0)
	            resto = 1
	        elif(bina1[i] == 1 and bina2[i] == 1 and resto == 1):
	            risultato.append(1)
	            resto = 1
	        elif(bina1[i] == 0 and bina2[i] == 0 and resto == 0):
	            risultato.append(0)
	            resto = 0
	        i = i - 1
	    risultato.reverse()
	    print("Risultato: ", risultato)
	    print("Overflow = ", resto)
	
	
	
	# -----MAIN-----
	n = nBit() #richiamo la funzione per definire il numero di bit e assegno il risultato a n
	
	#con n definito richiamo la funzione per inserire i bit (0 e 1) nei 2 arrey
	print("\nInserisci il 1º numero binario\n------------------------------")
	inser(binario1)
	print("\nInserisci il 2º numero binario\n------------------------------")
	inser(binario2)
	
	
	print("Binario 1: ",binario1)
	print("Binario 2: ",binario2)
	somma(binario1, binario2)

--
####6.4 Conversione Decimale-Binario su un numero fisso di bit
Scrivere un programma in linguaggio Py che converta un numero decimale D in un
numero binario rappresentato su N bit.
L’utente inserisce un numero decimale intero positivo D e il numero N di bit su cui il
numero decimale deve essere rappresentato.
Il programma visualizzerà i bit che compongono il numero binario partendo dal bit meno significativo.
Il programma segnalerà un errore se il numero N di bit inserito dall’utente non è
sufficiente per rappresentare il numero decimale.

Suggerimento. Per effettuare la conversione usare il metodo delle divisioni successive.
Ad esempio, per convertire il numero decimale D=19 su N=7 bit, si avrà:

	Numero      Resto       Cifra binaria       Peso
	19          1 (19%2)    1                   0
	9 (19/2)    1 (9%2)     1                   1
	4 (9/2)     0 (4%2)     0                   2
	2 (4/2)     0 (2%2)     0                   3
	1 (2/2)     1 (1%2)     1                   4
	0 (1/2)     0 (0%2)     0                   5
	0 (0/2)     0 (0%2)     0                   6


Nota: nell’applicazione del metodo delle divisioni successive, l’iterazione termina quando
è stato assegnato un valore a ciascuno degli N bit.

####Soluzione
	# -----VARIABILI-----
	D = 0
	n = 0
	length = 0
	i = 0
	# -------------------
	
	def conversione(x,y):
	    #print(x, " ", y)
	    bina=[]
	    resto = 0
	    j = 0
	    l = 0
	    length = 0
	    while(j <= y-1 and x > 0):
	        resto = int(x) % 2
	        x = int(x) / 2
	        bina.append(resto)
	        j = j + 1
	    length = len(bina)
	    if(x > 0 and j > y-1):
	        print("numero N di bit inserito non è sufficiente per rappresentare il numero decimale: ", end='')
	        for l in range(length):
	            print(bina[l], end=' ')
	        print("...")
	    else:
	        for l in range(length):
	            print(bina[l], end=' ')
	
	
	
	# -----MAIN-----
	while(i == 0): #ciclo sempre vero 
	    if(D > 0 and n > 0):
	        conversione(D, n)
	        exit() #per uscire dal programma appena ha concluso la funzione
	    else:
	        while(D <= 0):
	            try:
	                D = int(input("Inserisci il numero decimale intero positivo da convertire: "))
	            except ValueError:
	                print("ERRORE. Inserisci un numero decimale intero positivo")
	
	        while(n <= 0):
	            try:
	                n = int(input("N di bit su cui il numero decimale deve essere rappresentato: "))
	            except ValueError:
	                print("ERRORE. Inserisci un numero maggiore di 0")
--
####6.5 Ricerca di un elemento in vettore
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
I numeri sono memorizzati in un vettore.
Il valore N è inserito dall’utente, ma il vettore può contenere al massimo 30 numeri.

Terminato l’inserimento della sequenza di numeri, l’utente inserisce un valore di riferimento.
Il programma deve indicare se tale valore di riferimento è contenuto nel vettore.
####Soluzione

	# -----VARIABILI-----
	n = 0
	# -------------------
	def nInteri():
	    global n
	    length = 30
	    while(n <= 0):
	        try:
	            n = int(input("Inserisci N:"))
	            if(n > length):
	                print("ERRORE. Non c'è spazio per ",n, "elementi.")
	                n = 0
	            elif(n <= 0):
	                print("ERRORE. Inserisci un numero intero positivo > 0")
	        except ValueError:
	            print("ERRORE. Inserisci un numero intero positivo <= 30")
	    return n
	
	def memory(x):
	    i = 0
	    array = []
	    elem = 0
	    print("Inserisci ", x, "numeri interi")
	    for i in range(x):
	        print("elemento della Lista numero ", i, ":", end='')
	        elem = int(input())
	        array.append(elem)
	    return array
	
	def search(arr, x):
	    ser = False
	    r = i = 0
	    count = 0
	    found = []
	    r = int(input("Inserisci il valore da ricercare: "))
	    for i in range(x):
	        if(arr[i] == r):
	            found.append(i+1)
	            ser = True
	    if(ser == False):
	        print("Elemento non presente nella lista.")
	    else:
	        count = len(found)
	        print("\nElemento TROVATO.\n E' presente ", len(found), "volte nelle posizioni ", found)
	
	# -----MAIN-----
	
	f = nInteri()
	vett = memory(f)
	search(vett, f)
--
####6.6 Verificare se un vettore contiene tutti elementi tra loro uguali
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
I numeri sono memorizzati in un vettore.
Il valore N è inserito dall’utente, ma il vettore può contenere al massimo 30 numeri.
Terminato l’inserimento della sequenza di numeri, il programma deve verificare se gli elementi
del vettore sono tutti uguali tra loro.
####Soluzione
	# -----VARIABILI-----
	n = 0
	# -------------------
	def nIns():
	    n = 0
	    while(n <= 0):
	        try:
	            n = int(input("Inserisci N:"))
	            if(n <= 0):
	                print("ERRORE. Inserire un valore maggiore di 0")
	            elif(n > 30):
	                print("ERRORE. Inserire un valore minore di 30")
	                n = 0
	        except ValueError:
	            print("ERRORE. Valore non permesso")
	    return n
	
	
	def cont(array, x):
	    flag = 0
	    i = 0
	    j = 1
	    while(i < x-1):
	        if(array[i]==array[j]):
	            flag += 1
	        else:
	            flag = 0
	        i += 1
	        j += 1
	
	    if(flag == x-1):
	        print("\nL'array contiene tutti gli elementi uguali")
	    else:
	        print("\nL'array NON contiene tutti gli elementi uguali")
	
	
	def insVett():
	    n = nIns()
	    i = 0
	    x = 0
	    vett = []
	    print("Inserisci",n, "valori nell'array")
	    for i in range(n):
	        print("Inserisci nella posizione",i,"dell'array:", end='')
	        x = int(input())
	        vett.append(x)
	    cont(vett, n)
	
	
	
	# -----MAIN-----
	
	insVett()
--
####6.7 erificare se un vettore di interi è ordinato
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
I numeri sono memorizzati in un vettore.
Il valore N è inserito dall’utente, ma il vettore può contenere al massimo 30 numeri.
Terminato l’inserimento della sequenza di numeri, il programma deve verificare se il
vettore contiene una sequenza di numeri ordinata in modo strettamente crescente.
####Soluzione
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
--
####6.8 Stampa istogrammi
Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
Il valore N è inserito dall’utente.
I numeri sono memorizzati in un vettore.
Terminato l’inserimento della sequenza di numeri, il programma deve visualizzare una
riga di asterischi per ogni numero inserito.
Il numero di asterischi nella riga è pari al valore del numero inserito.

Ad esempio, dato il vettore 9 4 6 il programma deve visualizzare:

	            Elemento 1: 9 *********
	            Elemento 2: 4 ****
	            Elemento 3: 6 ******
####Soluzione
	def nIns():
	    x = 0
	    while(x <= 0):
	        try:
	            x = int(input("Inserisci il numero di istogrammi da rappresentare: "))
	            if(x <= 0):
	                print("ERRORE. Inserisci un valore maggiore di 0")
	        except ValueError:
	            print("ERRORE. Valore inserito non consentito\nRiprova")
	    return x
	
	def memory():
	    n = nIns()
	    vett = []
	    i = 0
	    while(i < n):
	        try:
	            print("Inserisci un valore per la posizione",i,"dell'array: ",end='')
	            num = int(input())
	            if(num < 0):
	                print("ERRORE. Inserisci un numero intero maggiore di 0")
	            else:
	                vett.append(num)
	                i += 1
	        except ValueError:
	            print("ERRORE. Valore non valido!")
	    return vett
	
	def asterisk(vett, ind):
	    i = j = 0
	    for i in range(ind):
	        print("Elemento",i+1,":",vett[i],end=' ')
	        k = 0
	        j = vett[i]
	        while(k < j):
	            print("*",end='')
	            k += 1
	        print()
	
	# -----MAIN-----
	array = memory()
	asterisk(array, len(array))
--
####6.9 Calcolo dell’opposto di un numero binario rappresentato in complemento a 2 su N bit
Scrivere un programma che riceve in ingresso un numero binario rappresentato in complemento a 2 su N bit.
Inizialmente l’utente inserisce il numero N di bit.
Quindi inserisce le cifre del numero binario un bit alla volta, partendo dal bit più significativo (MSB).

Terminato l’inserimento del numero, il programma esegue le seguenti operazioni:

1. visualizza il numero inserito partendo dal bit più significativo
2. calcola l’opposto del numero binario ricevuto in ingresso
3. visualizza l’opposto del numero binario ricevuto in ingresso partendo dal bit più significativo (MSB).

Per poter effettuare il calcolo del risultato, utilizzare il metodo secondo
il quale si considerano le cifre del numero binario in complemento a
due, invertite e successivamente sommato 1.

	N = 10
	Binario Negativo: 1111110011
	         Opposto: 0000001100 (+1)
	Binario Positivo: 0000001101
	        Decimale: 11

####Soluzione
	# -----VARIABILI-----
	bina = []
	n = 0
	# -------------------
	
	def nIns():
	    x = 0
	    while(x <= 0):
	        try:
	            x = int(input("inserisci il numero N di bit: "))
	            if(x <= 0):
	                print("ERRORE. Inserisci un numero N di bit intero e positivo")
	        except ValueError:
	            print("ERRORE. Riprova!")
	    return x
	
	def stam(array,x):
	    i = 0
	    for i in range(x):
	        print(array[i], end=' ')
	
	def binarioCom2():
	    global n
	    n = nIns()
	    j = 1
	    i = 0
	    global bina
	    print("inserisce le cifre del numero binario un bit, partendo dal bit più significativo")
	    while(i < n):
	        try:
	            print("Inserisci il bit in posizione",j,":",end='')
	            elem = int(input())
	            if(elem > 1 or elem < 0):
	                print("ERRORE. Valori permessi: 0 e 1")
	            else:
	                bina.append(elem)
	                i += 1
	                j += 1
	        except ValueError:
	            print("ERRORE. Valore non corretto!")
	    #print(bina)
	
	    print("\nInserito: ",end='')
	
	    stam(bina,n)
	    if(bina[0] == 0):
	        print("\n\nUn numero binario negativo non può avere il bit più significativo uguale a 0")
	        print("Cambio il bit più significatico uguale a 0 con 1...")
	        bina[0] = 1
	        print("\nAggiornato: ",end='')
	        stam(bina,n)
	    #return bina
	
	def binario(array):
	    length = len(array)-1
	    while(length >= 0):
	        if(array[length] == 0):
	            array[length] = 1
	        elif(array[length] == 1):
	            array[length] = 0
	        length -= 1
	    print("\nOpposto: ",end=' ')
	    stam(bina,n)
	
	def somma1(array,x):
	    i = x-1
	    rest = 1
	    while(i >= 0):
	        if((array[i]==1 and rest==0) or (array[i]==0 and rest==1)):
	            array[i] = 1
	            rest = 0
	        elif(array[i]==1 and rest==1):
	            array[1] = 0
	            rest = 1
	        else:
	            array[i] = 0
	            rest = 0
	        i -= 1
	    print("\nBinario: ",end=' ')
	    stam(array,x)
	
	# -----MAIN-----
	binarioCom2()
	binario(bina)
	somma1(bina,n)

--
####6.10 Operazione di shift di un vettore

Scrivere un programma in linguaggio Py che riceve in ingresso una sequenza di N numeri interi.
Il valore N è inserito dall’utente.
I numeri sono memorizzati in un vettore.
Il programma esegue le seguenti operazioni:

   1. visualizza il vettore
   2. esegue uno spostamento (shift) a sinistra di una posizione del contenuto del vettore.
        Pertanto ogni elemento del vettore deve assumere il valore dell’elemento immediatamente
        successivo all’interno del vettore. L’elemento di indice N-1 deve assumere il valore zero.
        Ad esempio dato il vettore: 1 10 15 18
        Il programma deve generare il vettore: 10 15 18 0
        Il programma visualizza il vettore ottenuto.
   3. esegue uno spostamento (shift) a destra di una posizione del contenuto del vettore ottenuto
        nel passo precedente. Pertanto ogni elemento del vettore deve assumere il valore dell’elemento
        immediatamente precedente all’interno del vettore. L’elemento di indice 0 deve assumere il valore zero.
        Ad esempio dato il vettore: 10 15 18 0
        Il programma deve generare il vettore: 0 10 15 18
        Il programma visualizza il vettore ottenuto.

Nota. Nella definizione di “destra” e “sinistra” si immagini il vettore stampato orizzontalmente,
a partire dalla cella di indice 0.
####Soluzione
	# -----VARIABILI-----
	n = 0
	array = []
	s = 0
	# -------------------
	def nIns():
	    global n
	    while(n <= 0):
	        try:
	            n = int(input("Inserisci un valore N: "))
	            if(n <= 0):
	                print("ERRORE. Inserire un valore maggiore di 0")
	                n = 0
	        except ValueError:
	            print("ERRORE. Valere non concesso")
	
	def stamp(vett,x):
	    i = 0
	    for i in range(x):
	        print(vett[i], end=' ')
	
	def memory(vett,x):
	    i = 0
	    app = 0
	    print("\ninserisci",x,"elementi nell'array")
	    while(i < x):
	        try:
	            print("Elemento",i+1,":",end='')
	            app = int(input())
	            if(app < 0):
	                print("ERRORE. Inserisci un valore intero maggiore di 0")
	            else:
	                vett.append(app)
	                i += 1
	        except ValueError:
	            print("ERRORE. Valore inserito non concesso")
	    stamp(vett,x)
	
	def sx(vett, x):
	    i = 0
	    j = 1
	    print("              Ingresso: ",end='')
	    stamp(vett,x)
	    while(j < x):
	        vett[i] = vett[j]
	        j += 1
	        i += 1
	    if(j == x):
	        vett[j-1] = 0
	    print("\nSpostamento a Sinistra: ",end='')
	    stamp(vett,x)
	
	def dx(vett, x):
	    i = x-1
	    j = x-2
	    print("            Ingresso: ",end='')
	    stamp(vett,x)
	    while(j >= 0):
	        vett[i] = vett[j]
	        j -= 1
	        i -= 1
	    if(j < 0):
	        vett[0] = 0
	    print("\nSpostamento a Destra: ",end='')
	    stamp(vett,x)
	
	# -----MAIN-----
	nIns()
	memory(array,n)
	
	print("\n\nSeleziona il tipo di spostamento\n1: sinistra\n2: destra")
	s = int(input())
	if(s == 1):
	    sx(array,n)
	elif(s == 2):
	    dx(array, n)

--
####6.11 Compattazione di un vettore
Scrivere un programma in linguaggio Py che legge N numeri interi da tastiera e li memorizza in un vettore.
Il numero N viene inserito dall’utente ed è minore di 20.
Il programma deve generare un secondo vettore che compatta i numeri contenuti nel primo vettore.
In particolare:

- ogni numero che compare ripetuto nel primo vettore, deve comparire una sola volta nel secondo vettore
- ogni numero uguale a zero presente nel primo vettore non deve comparire nel secondo vettore.
Il programma deve visualizzare il contenuto del secondo vettore.

Esempio 1: si supponga N=8 e si consideri la sequenza di numeri 1 18 3 0 24 3 6 0 inseriti da tastiera.
Il programma deve visualizzare 1 18 3 24 6.

Esempio 2: si supponga N=10 e si consideri la sequenza di numeri 1 18 3 0 0 24 3 6 0 3 inseriti da tastiera.
Il programma deve visualizzare 1 18 3 24 6.  
####Soluzione
	# -----VARIABILI-----
	array = []
	n = 0
	# -------------------
	def nIns():
	    global n
	    print("Inserisci un valore > 0 < 20")
	    while(n <= 0):
	        try:
	            n = int(input("Inserisci N:"))
	            if(n <= 0 or n > 20):
	                print("ERRORE. Inserisci un valore > di 0 e < 20")
	                n = 0
	        except ValueError:
	            print("ERRORE. Valore inserito non corretto")
	
	def stamp(vett,x):
	    i = 0
	    for i in range(x):
	        print(vett[i],end=' ')
	    print()
	
	def memory(vett,x):
	    i = 0
	    elem = 0
	    print("Inserisci",x,"elementi nell'array")
	    while(i < x):
	        print("Elemento",i+1,":",end='')
	        try:
	            elem = int(input())
	            if(elem >= 0):
	                vett.append(elem)
	                i += 1
	            else:
	                print("ERRORE. Inserisci numeri interi positivi")
	        except ValueError:
	            print("ERRORE. Sono permessi solo numeri interi positivi\nRiprova")
	    print("\nINGRESSO:",end=' ')
	    stamp(vett,x)
	
	def del0(vett,x):
	    i = 0
	    while(i < x):
	        if(vett[i] == 0):
	            del vett[i]
	        else:
	            i += 1
	        if(x != len(vett) or x == x):
	            x = len(vett)
	
	def compatt(vett,x):
	    del0(vett,x)
	    i = 0
	    app = 0
	    while(i < x):
	        j = 0
	        app = vett[i]
	        while(j < x):
	            if(app == vett[j] and j != i):
	                del vett[j]
	            if(x != len(vett)):
	                x = len(vett)
	            j += 1
	        i += 1
	    print("COMPATTO:",end=' ')
	    stamp(vett,x)
	
	# -----MAIN-----
	nIns()
	memory(array,n)
	compatt(array,n)
--
####6.12 Intersezione di due vettori
Siano dati due vettori di interi inseriti da tastiera.
La lunghezza dei due vettori è inserita dall’utente da tastiera.
I due vettori possono avere lunghezze diverse, ma possono contenere al massimo 30 numeri.
Si scriva un programma in linguaggio Py per generare un terzo vettore che contiene l’intersezione
tra due vettori. Tale vettore deve contenere i numeri presenti in entrambi i vettori dati.

	Ad esempio, si assuma che siano stati inseriti i due vettori:
	1 6 15 20 25
	2 20 18 6
	
	Il programma deve visualizzare la sequenza 
	6 20.

####Soluzione
	# -----VARIABILI-----
	n = 0
	n1 = 0
	array1 = []
	array2 = []
	array3 = []
	# -------------------
	def nIns():
	    x = 0
	    while(x <= 0):
	        print("Inserisci:",end=' ')
	        try:
	            x = int(input())
	            if(x <= 0):
	                print("ERRORE. Inserisci un valore intero maggiore di 0")
	            elif(x > 30):
	                print("ERRORE. Inserisci un valore minore di 30")
	                x = 0
	        except ValueError:
	            print("ERRORE. Inserisci un valore intero maggiore di 0")
	    return x
	
	def stamp(vett):
	    x = len(vett)
	    i = 0
	    for i in range(x):
	        print(vett[i],end='; ')
	    print()
	
	def vettIns(vett,x):
	    i = 0
	    while(i <= x-1):
	        print("Inserisci un valore intero positivo nella posizione",i+1,":",end='')
	        elem = int(input())
	        vett.append(elem)
	        i += 1
	
	def compares(vett1,vett2):
	    global array3
	    i = j = app = 0
	    for i in range(len(vett1)):
	        app = vett1[i]
	        for j in range(len(vett2)):
	            if(vett2[j] == app):
	                array3.append(app)
	
	# -----MAIN-----
	print("Inserisci la lunghezza del primo Array")
	n = nIns()
	print("Inserisci la lunghezza del secondo Array")
	n1 = nIns()
	print("Inserisci",n,"valori all'interno del primo Array")
	vettIns(array1,n)
	print("Inserisci",n1,"valori all'interno del secondo Array")
	vettIns(array2,n1)
	
	print("VALORI INSERITI\nArray1:",end=' ')
	stamp(array1)
	print("Array2:",end=' ')
	stamp(array2)
	print("\nIntersezione tra i due vettori:")
	compares(array1,array2)
	stamp(array3)
