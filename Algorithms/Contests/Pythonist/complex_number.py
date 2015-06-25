__author__ = 'ramvibhakar'
import math

class Complex(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0 and self.b != 0:
            return format(self.b,'.2f')+'i'
        if self.b > 0:
            return format(self.a, '.2f')+' + '+format(self.b, '.2f')+'i'
        elif self.b < 0:
            return format(self.a, '.2f')+' - '+format(abs(self.b), '.2f')+'i'
        else:
            return format(self.a,'.2f')
    def __add__(self,rhs):
       return Complex(self.a + rhs.a, self.b + rhs.b)

    def __sub__(self,rhs):
        return Complex(self.a - rhs.a, self.b - rhs.b)

    def __mul__(self,rhs):
        return Complex(self.a*rhs.a - rhs.b*self.b, self.b*rhs.a + rhs.b*self.a)

    def __div__(self,rhs):
        conjug = Complex(rhs.a,-rhs.b)
        denom = rhs * conjug
        num = self * conjug
        return Complex(num.a/denom.a,num.b/denom.a)
    def __abs__(self):
        return format(math.sqrt(self.a**2 + self.b**2),'.2f')

a,b =[float(x) for x in raw_input().split()]
comp1 = Complex(a,b)
a,b =[float(x) for x in raw_input().split()]
comp2 = Complex(a,b)
print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 / comp2)
print(abs(comp1))
print(abs(comp2))