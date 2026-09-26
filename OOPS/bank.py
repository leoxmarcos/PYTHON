class Bank:
    def __init__(self):
        self.balance = 0
        self.pin = " "

        self.menu()

    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()
        else:
            print("Invalid input")
            self.menu()


    def create_pin(self):
        self.pin = input("Enter a new pin: ")
        print("Pin created successfully")
        self.menu()
   

    def deposit(self):
        tempin = input("Enter your pin: ")
        if tempin == self.pin:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Incorrect pin")
        self.menu()


    def withdraw(self):
        tempin = input("Enter your pin: ")
        if tempin != self.pin:
            print("Incorrect pin")
            return
        else:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        self.menu()


    def check_balance(self):
        tempin = input("Enter your pin: ")
        if tempin == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Incorrect pin")
        self.menu()
    
    def exit(self):
        print("Thank you for using our services")
      


# calling the constructor to create an object of the class
sbi = Bank()
sbi.menu()
id(sbi)

# constructor->magic method->predefined method->dunder method (double underscore method)
# object don't call the magic method directly, it is called automatically triggered when the object is created.
# constructor ->database connection, file handling,hardware connectivity, network connection, etc. (initialization of the object)
# which object you are working i.e self->current object
# why self is important->to access the attributes and methods of the class in python, we need to use self.
# class can't access of it's own attributes and methods without self.It needs object to access it's own attributes and methods.




