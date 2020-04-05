import math

a=float(input('Podaj dlugosc pierwszej przyprostokatnej: '))
b=float(input('podaj dlugosc drugiej przyprostokatnej: '))
def pitagoras(a,b):
    return math.sqrt((a)**2+(b)**2)

print(pitagoras(a,b))