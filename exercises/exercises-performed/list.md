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
- 3.9 massimo comune divisore tra 2 numeri


### **4 Funzioni**
- 4.1 Moltiplicazione
- 4.2 Anagrafica
- 4.3 Dentro e fuori dalla funzione
- 4.5 Valore Assoluto
- 4.6 Potenza di N
- 4.7 Calcolo del massimo
- 4.8 Calcolo del massimo a 3
- 4.9 Quadrati perfetti






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
####3.9 massimo comune divisore tra 2 numeri
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
