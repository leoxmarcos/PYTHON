name=input("whats your name?")
# print("hello,")
# print(name)

# return value
# name = input("Whats your name? ")
# # print("hello, ",name)
# print("hello, " + name) #concatenation


# print (objects,sep='',end='\n')
# print("hello," , end="???")
# print(name)

# print("hello," , name, sep="???")#seperator


# print(f"hello,  {name}")


#Remove white space from string
name=name.strip()

# Capitalize user's name just the first letter
name=name.capitalize()

# Title is used to capitalize the first letter of each word
# name=name.title()

# split user name into first name and the last name
first, last = name.split(" ")

print(f"hello, {first}")







