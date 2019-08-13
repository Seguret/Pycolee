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










