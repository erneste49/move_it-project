
#Example of multiple inheritance, passing multiple parent class to class Shape
class Circle:
    def ci_sides(self):
        print("A circle has one side")
        
class Triangle():
    def tr_sides(self):
        print("A triangle has 3 sides")
        
class Square():
    def sq_sides(self):
        print("A square has 4 sides")
    
class Shape(Circle, Triangle, Square):
    def sh_sides(self):
        print("A shape have some sides")
        
sh = Shape()
sh.sh_sides()
sh.ci_sides()
sh.tr_sides()
sh.sq_sides()