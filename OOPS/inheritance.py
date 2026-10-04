#inheritance gives code reusability.
#Inheritance allows a class to acquire the data members ,properties, constructors and methods of another class but not private members.
class user:
    def login(self,username,password):
        self.username=username
        self.password=password
        print("User logged in successfully")
    def logout(self):
        print("User logged out successfully")
class student(user):
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
student1=student("Ramesh",101)
student1.login("ramesh123","password123")
student1.display()
student1.logout()
 
