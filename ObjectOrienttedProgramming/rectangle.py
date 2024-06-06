class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print("Area of Rectangle: {}".format(area))
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("Perimeter of Rectangle: {}".format(perimeter))
rectangle = Rectangle(2.5,5.1)
rectangle.area()
rectangle.perimeter()

# output: Area of Rectangle: 12.75
#         Perimeter of Rectangle: 15.2