#stampa informazioni di un utente inserite da tastiera


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
