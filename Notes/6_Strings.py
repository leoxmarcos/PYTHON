#string methods
print("hello".upper())
print("HELLO".lower())
print("hello".capitalize())
print("hello honey".title())

#strip->removes whitespace from the beginning and end of the string
print("   hello honey   ".strip())

#replace->replaces a substring with another substring
print("hello honey".replace("honey","sweetheart"))

#split->splits a string into a list of substrings based on a delimiter
print("hello honey".split(" "))

#find->returns the index of the first occurrence of a substring, or -1 if not found
print("hello honey".find("ey"))

#count->returns the number of occurrences of a substring in a string
print("hello honey".count("o"))

#startswith->returns True if the string starts with the specified substring, otherwise False
print("hello honey".startswith("h"))

#endswith->returns True if the string ends with the specified substring, otherwise False
print("hello honey".endswith("y"))

#isalpha->returns True if all characters in the string are alphabetic, otherwise False
print("hello".isalpha())
print("hello123".isalpha())

#isdigit->returns True if all characters in the string are digits, otherwise False
print("123".isdigit())

#zfill->pads the string with zeros on the left until it reaches the specified width
print("123".zfill(5))

#string formatting
name="John"
print("Hello, my name is {}".format(name))
print(f"Hello, my name is {name}")
print("Hello, my name is %s" % name)

#escape characters
print("Hello\nWorld") #next line
print("Hello\tWorld") #tab
print("Hello\\World") #backslash
print("Hello\"World\"") #double quotes
print("Hello\'World\'") #single quotes
print("hello\b honey") #backspace
print("Hello\rHii") #carriage return
print("hello\fhoney") #form feed
print("Hello\vPython") #vertical tab
print("\a") #bell/alert

#raw strings
print(r"Hello\nWorld") #raw string, ignores escape characters

#string multiplication
print("hello "*3) #repeats the string 3 times
