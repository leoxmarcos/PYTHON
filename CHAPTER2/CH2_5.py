#OPERATORS IN PYTHON
#Arithmetic Operators
a=10
b=3
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Exponentiation:", a**b)

#Comparison Operators
print("Is a equal to b?", a==b)
print("Is a not equal to b?", a!=b)
print("Is a greater than b?", a>b)
print("Is a less than b?", a<b)
print("Is a greater than or equal to b?", a>=b)
print("Is a less than or equal to b?", a<=b)

#Logical Operators
x=True
y=False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)

#Assignment Operators
c=5
c+=2  #c=c+2
print("c after +=2:", c)
c*=3  #c=c*3
print("c after *=3:", c)
c-=4  #c=c-4
print("c after -=4:", c)
c//=2  #c=c//2
print("c after //=2:", c)

#Bitwise Operators
m=5  #Binary: 0101
n=3  #Binary: 0011
print("m & n (AND):", m & n)  #Binary: 0001
print("m | n (OR):", m | n)   #Binary: 0111
print("m ^ n (XOR):", m ^ n)  #Binary: 0110
print("~m (NOT):", ~m)         #Binary: 1010
print("m << 1 (Left Shift):", m << 1)  #Binary: 1010
print("m >> 1 (Right Shift):", m >> 1) #Binary: 0010

#Membership Operators
str1="Hello, welcome to Python programming."
print("'Python' in str1:", 'Python' in str1)
print("'Java' not in str1:", 'Java' not in str1)

#Identity Operators
p=[1,2,3]
q=p
r=[1,2,3]
print("p is q:", p is q)
print("p is r:", p is r)
print("p is not r:", p is not r)