class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_city,new_pin,new_state,new_name=None):
        if new_name is not None:
            self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)
class address:
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pin=new_pin
        self.state=new_state
address1=address("Bangalore",560001,"Karnataka")
customer1=customer("Ramesh","Male",address1)
customer1.edit_profile(new_city="Mysore",new_pin=570001,new_state="Karnataka")
print(customer1.name)
print(customer1.gender)
print(customer1.address.city)
print(customer1.address.pin)
print(customer1.address.state)

#class aggregation refers to has-a relationship between two classes.  
#class inheritance refers to is-a relationship between two classes.