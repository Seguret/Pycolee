# **Esercizi di Programmazione in Python**
Esercitazioni per il progetto **Pycolee**


## **INDICE**

### **1 Primo programma in Py**
- 1.1 Somma di due numeri
- 1.2 Precedente e Successivo
- 1.3 Media tra due numeri
- 1.4 Semplice calcolatrice
- 1.5 calcolo di aree





--
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




