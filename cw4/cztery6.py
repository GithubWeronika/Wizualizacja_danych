##Zad.6 Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
##sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
##sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
##sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
##wyświetl_wyrazy – wyświetla podane wyrazy
##Stwórz instancję klasy i sprawdź działanie wszystkich metod.
class Slowa:
    def __init__(self, slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def sprawdz_czy_palindrom(self,slowo1,slowo2):
        if slowo1==slowo1[::-1]:
            print("Slowo1 jest palindromem")
        else:
            print("Slowo1 nie jest palindromem")
        if slowo2==slowo2[::-1]:
            print("Slowo2 jest palindromem")
        else:
            print("Slowo2 nie jest palindromem")
    def sprawdz_czy_metagramy(self,slowo1,slowo2):
        i=0
        if slowo1!=slowo2[::-1]:
            i+=1
            if i>1:
                print("Nie sa metagramami")
            if i<1:
                print("Sa metagramami")
        else:
            print("Nie sa metagramami")
    def sprawdz_czy_anagramy(self,slowo1,slowo2):
        if slowo1[::]!=slowo2[::]:
            print("Nie sa anagramami")
    def wyswietl_wyrazy(self,slowo1,slowo2):
        print(slowo1)
        print(slowo2)
wyraz=Slowa('Kajak','tatar')
wyraz.wyswietl_wyrazy('Kajak','tatar')
print(wyraz.sprawdz_czy_anagramy('Kajak','tatar'))
print(wyraz.sprawdz_czy_metagramy('Kajak','tatar'))
print(wyraz.sprawdz_czy_palindrom('Kajak','tatar'))



        