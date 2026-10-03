num1=[1,2,3,4,5,6]
num2=[6,5,4,3,2,1]
ans=[]


# for i in range(len(num1)):
#     ans.append(num1[i]+num2[i])
# print(ans)


# list comprehension
ans = [num1[i] + num2[i] for i in range(len(num1))]

print(ans)


# revese the number
num=234567
result=0;

while num>0:
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)

#sum of digits
num=12345
result=0
while num>0:
    digit=num%10
    result=result+digit
    num=num//10 
print(result)

