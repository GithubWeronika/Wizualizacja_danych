##Zad.1 Wygeneruj liczby podzielne przez 4 i zapisz je do pliku
import random
##liczba1=random.randint(0,100)
##liczba2=random.randint(0,100)
##liczba3=random.randint(0,100)
##if liczba1%4==0:
    ##print("Tak")
##else:
    ##print("Nie")
liczby=[random.randint(0,100) for k in range (0,100)]
podzielne=[k for k in liczby if k%4==0]
print("To są liczby podzielne przez 4:")
print(podzielne)
plik=open("podzielne.txt","a+")
plik.writelines(str(podzielne))
plik.close()