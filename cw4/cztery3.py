##Zad.3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
import sys
with open("dane.txt", "w+") as plik:
    ##print("Podaj jakiś tekst")
    ##test=sys.stdin.readline()
    test="n123o odczytaj to w koncu proooszeee"
    for napis in test:
        plik.write(napis)
with open("dane.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
    