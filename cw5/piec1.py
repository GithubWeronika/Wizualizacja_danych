class Material:
    # definicja konstruktora
    def __init__(self, rodzaj, dlugosc,szerokosc):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.rodzaj=rodzaj 
        self.dlugosc=dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):
    # definicja konstruktora
    def __init__(self, rozmiar, kolor,dla_kogo):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.rozmiar=rozmiar 
        self.kolor=kolor
        self.dla_kogo = dla_kogo
    def wyswietl_dane(self):
        print(self.rozmiar)
        print( self.kolor)
        print(self.dla_kogo)
class Sweter(Ubrania):
    # definicja konstruktora
    def __init__(self, rodzaj_swetra):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        print(self.rodzaj_swetra)
material1 = Material('tkanina gladka', 2, 2)
material2 = Material('zwykla tkanina', 1, 1)
material3 = Material('tkanina sliska', 8, 8)
material1.wyswietl_nazwe()
material2.wyswietl_nazwe()
material3.wyswietl_nazwe()

ubranie = Ubrania('M', 'rozowe', 'pan Stefan')
ubranie.wyswietl_dane()

