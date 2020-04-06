##Zad.10 Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartosc to ilosc. Funkcja ma zliczyc ile jest wszystkich produktow
##w ogole i podawac ta wartosc
def ListaZakupow(** rzeczy):
    for cos in rzeczy:
        print("Oto lista")
        print(rzeczy[cos])
        ogorek=2
        pomidor=3
        chleb=1
        maslo=1
        jajka=10
        dzem=1
        mielonka_konserwowa=5
        suma=ogorek+pomidor+chleb+maslo+jajka+dzem+mielonka_konserwowa
        print("Suma wszystkiego:",suma)
ListaZakupow(lista="Ogorek=2,Pomidor=3,Chleb=1,Maslo=1,Jajka=10,Dzem=1,Mielonka konserwowa=5")