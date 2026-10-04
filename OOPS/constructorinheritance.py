class phone:
    def __init__(self,price,brand,camera):
        print("This is a phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
class smartphone(phone):
    pass
s=smartphone(1000,"Apple","12MP")
print("Price:",s.price)
print("Brand:",s.brand)
print("Camera:",s.camera)