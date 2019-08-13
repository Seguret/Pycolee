#stampare le lettere di una stringa una ad una. stampare il messaggio:
# la lettera X è "lettera" con la lettera di un altro colore

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

