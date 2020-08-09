"""Wyjaśnij, jak działa poniższa funkcja. Wyjaśnij, skąd
wzięły się wyniki zwrócone przez poszczególne
wywołania funkcji."""

def dodaj_do_listy(n, lista=[]):
    lista.append(n)
    print(lista)

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
#argument domyślny (lista) powstaje tylko raz, w momencie definiowania funkcji;
dodaj_do_listy(3) #output: [1, 3]