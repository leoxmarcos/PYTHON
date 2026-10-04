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
#you can inherit constructors.
#you cannot inherit private members of a class.
#method overriding is a feature of inheritance where a subclass can provide a specific implementation of a method that is already defined in its superclass.
#method overloading is a feature of inheritance where a subclass can have multiple methods with the same name but different parameters.
#operator overloading is a feature of inheritance where a subclass can provide a specific implementation of an operator that is already defined in its superclass.
#if child class has its own constructor then it will not inherit the constructor of parent class.