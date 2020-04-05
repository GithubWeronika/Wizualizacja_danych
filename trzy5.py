##Zad.5 rownolegle funkcje i prostopadle, lub ani jedne ani drugie
a1=float(input('podaj a1 '))
a2=float(input('podaj a2 '))

def wskaz(a1,a2):
    if a1*a2==-1:
        print('funkcje prostopadłe')
    elif a1==a2:
        print('funkcje równoległe')
    else :
        print('funkcje nie są ani równloległe ani prostopadłe')

print(wskaz(a1,a2))