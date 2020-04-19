##Zad.8 Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.
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
    def __del__(self):
        print("Obiekt zostal zniszczony")
    ##def pokaz_gdzie_jestes(self):
        ##print('Robaczek znajduje sie: ('str(self.x)','str(self.y)')')
gra=Robaczek(0,0,1)
print(gra.idz_w_gore(5))
print(gra.idz_w_dol(2))
print(gra.idz_w_prawo(20))
print(gra.idz_w_lewo(5))
##print(gra.pokaz_gdzie_jestes)