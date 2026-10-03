class Customer:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(Customer):
        if Customer.gender == "Male":
            print(f"Hello Mr. {Customer.name}")
        else:
            print(f"Hello Ms. {Customer.name}")
        
    
customer1 = Customer("John","Male")
new_cust=greet(customer1)
print(new_cust)
