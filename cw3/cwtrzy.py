## Zad.1 Zdefiniuj przykłady zbiorów, wykorzystując rozumienie Pythona
A=[1/x for x in (1,2,3,4,5,6,7,8,9,10)]
B=[2**x for x in (0,11,1)]
C=[x for x in B if x%4==0]
print(A)
print(B)
print(C)