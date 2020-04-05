##Zad.3 Utwórz słownik z produktami do kupienia
jednostkasztuka = {'dysk': 'szt','sok': 'l','papier': 'opakowanie',}
produktjednostka = {value: key for key, value in jednostkasztuka.items()}
print('Słownik:')
print(jednostkasztuka)
print('Zamiana miejsc:')
print(produktjednostka)