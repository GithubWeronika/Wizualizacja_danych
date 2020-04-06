##Zad.2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
with open("podzielne.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")