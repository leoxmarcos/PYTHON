name=(input("What's your name?"))

# if name=="Harry":
#     print("Gryffindor")
# elif name=="Hermaine":
#     print("Gryffindor")
# elif name=="Ron":
#     print("Gryffindo")
# elif name=="Draco":
#     print("Slytherin")
# else:
#     print("who ?")



# Using match and case key words

match name:
    case "Harry" | "Herminone" | "Ron":
        print("Gryffindo")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")