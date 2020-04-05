##Zad.2 Generowanie macierzy
import random
macierz = [[random.randint(0, 9) for j in range (0, 4, 1)] for i in range (0, 4, 1)]
przekatna = [macierz[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]
print('Macierz zawiera:')
print(macierz[0])
print(macierz[1])
print(macierz[2])
print(macierz[3])
print('Przekatna wynosi: ',przekatna)