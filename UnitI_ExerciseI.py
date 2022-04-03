'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit I, Exercise I
'''
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return ((math.pi)*((self.radius)**2))
        
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    def getVolume(self):
        area = super().getArea()
        return (area*self.height)

circle = Circle(4)
print("Circle area is: {:0.2f}".format(circle.getArea()))
cylinder = Cylinder(2, 5)
print("Cylinder volume is: {:0.2f}".format(cylinder.getVolume()))

'''
Execution results:
Circle area is: 50.27
Cylinder volume is: 62.83
'''