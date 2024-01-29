#Dictionar Hasing
persoane = {
    "ion" :
    {
        "nume" : "Ion",
        "varsta" : 30,
        "oras" : "Bucuresti"
    },
    "maria" :
    {
        "nume" : "Maria",
        "varsta" : 25,
        "oras" : "Suceava"

    },
    "andrei" :
    {
        "nume" : "Andrei",
        "varsta" : 18,
        "oras" : "Bacau"

    }
}
#Parcurgerea cheilor din dictionar
for cheie in persoane:
    print("Cheie: ",cheie)

#Parcurgerea valorilor asociate cu cheile;
for cheie in persoane:
    valoare = persoane[cheie]
    print("Valoarea asociata cheii ",cheie,":",valoare)

#Parcurgerea cheilor si a valorilor in acelasi timp
for cheie,valoare in persoane.items():
    print("Cheie: ",cheie)
    print("Valoare: ",valoare)
    