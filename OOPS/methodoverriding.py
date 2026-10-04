class phone:
    def __init__(self,price,brand,camera):
        print("this is parent class")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying a phone")
class product:
    def buy(self):
        print("buying a product")
class smartphone(phone,product):
    pass
s=smartphone(1000,"Apple","12MP")
s.buy()