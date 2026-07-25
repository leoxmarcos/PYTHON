def main():
    x=int (input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False

    #short form
    return n% 2 == 0

main()