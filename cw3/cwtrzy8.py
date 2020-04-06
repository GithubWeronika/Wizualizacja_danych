##Zad.8 Funkcja zwraca sume ciągu arytmetycznego
a1=1
r=1
ile_elementow=10
def suma(a1,r,ile_elementow):
    Sn=(2*a1+(ile_elementow-1)*r)/2*ile_elementow
    print(Sn)
print(suma(a1,r,ile_elementow))
