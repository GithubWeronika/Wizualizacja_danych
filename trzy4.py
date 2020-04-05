##Zad.4 Monotoniczność funkcji
a=float(input('okresl a '))

def jakafunkcja(a):
    if a>0:
        print('Jest rosnaca')
    if a==0:
        print('Jest stala')
    if a<0:
        print('Jest malejaca')

print(jakafunkcja(a))