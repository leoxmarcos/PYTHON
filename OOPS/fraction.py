class fraction:
    def __init__(self, n, d):
        self.numerator =n
        self.denominator =d


 #once the object is created, it will be called automatically when we print the object
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

        
    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)


    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)


    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return fraction(new_numerator, new_denominator)

    
x=fraction(1, 2)
print(x)

y=fraction(3, 4)
print(y)

z=x+y
print(z)

w=x-y
print(w)

v=x*y
print(v)

u=x/y
print(u)