##Zad.5 Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
##wyświetl_dane – drukuje elementy na ekran
##pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
##pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
##policz_sume – liczy sume elementow
##policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
##twórz instancję klasy i sprawdź działanie wszystkich metod.
class ciag:
    def __init__(self, n,r,a1):
        self.n=n
        self.r=r
        self.a1=a1
    def wyswietlf_dane(self,n,r,a1):
        for i=1 in i<n:
            wynik=i*r
            print(wynik)
            i++
    def pobierz_elementy(self,n,r,a1):
        self.a1=int(input('Podaj a1'))
        self.r=int(input('Podaj r'))
        self.n=int(input('Podaj n'))
    def policz_sume(self,n,r,a1):
        suma=(2*a1+(n-1)*r*n)/2
        print(suma)
    def policz_elementy(self,n,r,a1):
        for i=1 in i<n:
            liczba=a1+r
