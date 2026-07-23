# def hello(to="World"):
#     print("hello,",to)

# hello()
# name=input("What's your name? ")
# hello(name)

# def main():
#     name= input("What's your name? ")
#     hello()


# def hello(to="World"):
#     print("hello,",to )

# main()


def main():
    x= int(input("What's x? "))
    print("x squared is " , square(x))

def square(n):
    return pow(n,2)

main()