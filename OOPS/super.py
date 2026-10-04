class phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)

class smartphone(phone):
    def display(self):
        print("This is a smartphone.")
        super().display()

s=smartphone("Apple","Iphone 14")
s.display()
# The super() function is used to call the parent class's methods.