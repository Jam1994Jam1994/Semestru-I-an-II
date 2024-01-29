#Cautare_binara
def cautare_binara(lista, element):
    pozitii = []
    stanga = 0
    dreapta = len(lista) - 1

    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2

        if lista[mijloc] == element:
            pozitii.append(mijloc)
            # ontinuam cautarea......................................
            stanga_temp = dreapta_temp = mijloc

            while stanga_temp >= 0 and lista[stanga_temp] == element:
                pozitii.append(stanga_temp)
                stanga_temp -= 1

            while dreapta_temp < len(lista) and lista[dreapta_temp] == element:
                pozitii.append(dreapta_temp)
                dreapta_temp += 1

            break
        elif lista[mijloc] < element:
            stanga = mijloc + 1
        else:
            dreapta = mijloc - 1

    if not pozitii:
        # Elementul nu se regaseste in lista.................................
        return [-1]  
    else:
        return pozitii

# Introducerea listei de la tastatură
lista = [int(x) for x in input("Introduceti elementele listei separate prin spatiu: ").split()]

# Introducerea valorii de căutat de la tastatură
element = int(input("Introduceti valoarea de cautat: "))

rezultat =cautare_binara(lista, element)

if -1 in rezultat:
    print(f"Elementul {element} nu a fost gasit în lista.")
else:
    print(f"Elementul {element} a fost gasit la următoarele pozitii: {rezultat}.")
