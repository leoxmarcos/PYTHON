class Customer:
    def __init__(self, name):
        self.name = name
         
def greet(Customer):
    print(id(Customer))
    # Customer.name = "John"
    print(Customer.name)
    print(id(Customer))
cust=Customer("Mike")
print(id(cust))
greet(cust)
print(cust.name)

#list cloning
def change(L):
    print(id(L))
    L.append(4)
    print(id(L))
L1=[1,2,3]
print(id(L1))
print(L1)
change(L1[:])#clone of list is passed to function->no change in original list
print(L1)