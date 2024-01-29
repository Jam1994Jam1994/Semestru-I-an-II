#Cautare secventiala
def cautare_secventiala(lista, valoare):
    indexuri = []
    for i in range(len(lista)):
        if lista[i] == valoare:
            indexuri.append(i)
    return indexuri

# Solicitați utilizatorului sa introduca lista de numere separate prin spatii
lista = input("Introduceti lista de numere separate prin spatii: ").split()

# Modifica lista de siruri într-o lista de numere întregi
lista = [int(num) for num in lista]

# Solicitati utilizatorului sa introduca valoarea pe care doreste sa o caute
valoare_cautata = int(input("Introduceti valoarea pe care doriti sa o cautati: "))

rezultat = cautare_secventiala(lista, valoare_cautata)

if rezultat:
    print(f"Valoarea {valoare_cautata} a fost gasita la indexurile: {rezultat}")
else:
    print(f"Valoarea {valoare_cautata} nu a fost gasita în lista.")