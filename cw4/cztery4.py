##Zad.4 Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
##nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
##konstruktor – który nadaje wartości
##wyświetl_produkt() – drukuje informacje o produkcie na ekranie
##ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
##ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def konstruktor(self,nazwa_produktu,ilosc1,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa
        self.ilosc=ilosc
        self.jednostka_miary=jednostka
        self.cena_jed=cena
        nazwa=int(input('Podaj nazwe produktu '))
        ilosc1=int(input('Podaj ilosc '))
        cena=int(input('podaj cene '))
        jednostka=int(input('podaj jednostke '))
    def wyswietl_produkt(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        print("Nazwa produktu:")
        print(self.nazwa_produktu)
        print("Ilosc:")
        print(self.ilosc)
        print("Jednostka miary:")
        print(self.jednostka_miary)
        print("Cena za sztuke:")
        print(self.cena_jed)
    def ile_produktu(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        wynik=str(self.ilosc)+str(self.jednostka_miary)
        print(wynik)
    def ile_kosztuje(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        wynik1=self.ilosc*self.cena_jed
        print(wynik1)
produkt=NaZakupy('Chleb',2,'szkt',50)
produkt.wyswietl_produkt('Chleb',2,'szkt',50)
print("Ile produktu:")
print(produkt.ile_produktu('Chleb',2,'szkt',50))
print("Ile kosztuje:")
print(produkt.ile_kosztuje('Chleb',2,'szkt',50))

