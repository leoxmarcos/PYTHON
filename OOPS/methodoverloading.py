class geometry:
    def area(self, length=None, breadth=None, radius=None):
        if length is not None and breadth is not None:
            return length * breadth  # Area of rectangle
        elif radius is not None:
            return 3.14 * radius * radius  # Area of circle
        else:
            return "Invalid parameters"
obj=geometry()
# Area of rectangle
print("Area of rectangle:", obj.area(length=5, breadth=10))
# Area of circle
print("Area of circle:", obj.area(radius=7))