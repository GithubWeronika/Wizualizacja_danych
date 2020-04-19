##Zad.7 Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
##konstruktor – który nadaje wartość dla x, y i krok
##idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
##idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
##idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
##idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
##pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
##Stwórz instancję klasy i sprawdź jak działają wszystkie metody
class Robaczek:
    def __init__(self, x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow*self.krok
        wynik=ile_krokow*self.krok
        print("Robaczek przeszedl tyle krokow w gore:")
        print(wynik)
    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow*self.krok
        wynik=ile_krokow*self.krok
        print("Robaczek przeszedl tyle krokow w dol:")
        print(wynik)
    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow*self.krok
        wynik=ile_krokow*self.krok
        print("Robaczek przeszedl tyle krokow w prawo:")
        print(wynik)
    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow*self.krok
        wynik=ile_krokow*self.krok
        print("Robaczek przeszedl tyle krokow w lewo:")
        print(wynik)
    ##def pokaz_gdzie_jestes(self):
        ##print('Robaczek znajduje sie: ('str(self.x)','str(self.y)')')
gra=Robaczek(0,0,1)
print(gra.idz_w_gore(5))
print(gra.idz_w_dol(2))
print(gra.idz_w_prawo(20))
print(gra.idz_w_lewo(5))
##print(gra.pokaz_gdzie_jestes)