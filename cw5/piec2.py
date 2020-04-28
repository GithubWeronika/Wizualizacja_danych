class Ksztalty:
    def __init__(self, x):
        self.x = x
        self.y = x
    def mnozenie(self,ile):
        self.x=self.x*ile
        self.y=self.y*ile
    def kwadrat(self):
        self.x=self.x*self.x
        self.y=self.y*self.y
    def pole(self):
        return self.x*self.y

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self,other):
        return self.x+self.y

kw = Kwadrat(5)
kw2=Kwadrat(25)
kw3=Kwadrat(kw+kw2)
kw4=Kwadrat(kw2+kw3)
print('kw1:', kw.x,'x', kw.y,'y')
print('kw2:', kw2.x,'x', kw2.y,'y')
print('kw3:', kw3.x,'x', kw3.y,'y')
print('kw4:', kw4.x,'x', kw4.y,'y')
print(kw)