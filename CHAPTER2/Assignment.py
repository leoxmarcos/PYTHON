#Take input in celsius and convert it to fahrenheit and kelvin
celsius=float(input("Enter temperature in Celsius: "))
fahrenheit=(celsius*9/5)+32 
kelvin=celsius+273.15
print("Temperature in Fahrenheit:", fahrenheit) 
print("Temperature in Kelvin:", kelvin)

#Write a program that takes total bill amount and number of friends as input .calculate the amount each friend has to pay if the bill is split equally.
bill=float(input("Enter total bill amount: "))
friends=int(input("Enter number of friends: ")) 
amount_split=bill/friends
print("Each friend has to pay:", amount_split)
