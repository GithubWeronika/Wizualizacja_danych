#zad2, kalkulator
import sys
print("Podaj liczby: \n")
a=sys.stdin.readline()
b=sys.stdin.readline()
if(a>b):
    dzielenie=int(a)/int(b)
    print("Dzielenie")
    sys.stdout.write(str(dzielenie))
    odejmowanie=int(a)-int(b)
    print("------\n")
    print("Odejmowanie")
    sys.stdout.write(str(odejmowanie))
    print("------\n")
else:
    dzielenie2=b/a
    print("Dzielenie")
    sys.stdout.write(str(dzielenie2))
    print("------\n")
    print("Odejmowanie")
    odejmowanie2=int(b)-int(a)
    sys.stdout.write(str(odejmowanie2))
    print("------\n")
print("Dodawanie")
dodawanie=int(a)+int(b)
sys.stdout.write(str(dodawanie))
print("------\n")
print("Mnozenie")
mnozenie=int(a)*int(b)
sys.stdout.write(str(mnozenie))