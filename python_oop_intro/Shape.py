
class Rectangle:
    """This class calculates the area of a rectangle. The method collect needed value as parameter"""
    shape_name = "rectangle"
    
    def calculate_area(self, length, breadth):
        area = int(length) * int(breadth)
        return f"The area of length:{length} and breadth:{breadth} is = {area}"
    
#rectangle1 = Rectangle()
#print(rectangle1.calculate_area(10, 5))
#lth = input("Enter Length: ")
#bth = input("Enter breadth: ")
#print(rectangle1.calculate_area(lth, bth))

class Circle:
    """This class calculates the area and circumference of a circle with two attribute: pi and radius. Methods collect what they need via attribute"""
    pi = 3.142
    radius = None
    
    #constructor: is a magic method, it runs first | and authomatically and it is a donda method
    def __init__(self):
        print("i always run first and i run authomatically")
    
    def calculate_area(self ):
        return self.pi  * (self.radius**2)
    
        
        
    def calculate_circumference(self):
        cir = 2 * self.pi * self.radius
        return cir
    
#calculate area of a circle with radius of 7
#creating first object called circle1
circle1 = Circle()

circle1.radius = 7       # --> assigning value of 7 to attribute radius initially set to None

print(f"Area of circle1 = {circle1.calculate_area()}")
print("------------------------------------------------------------------------------")

#creating another object called circle2
circle2 = Circle()
circle2.radius = 21
print(f"Area of circle2 = {circle2.calculate_area()}")



















