class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width
        
    def rectangle_preimeter(self):
        return 2 * (self.length + self.width)
        
new_Rectangle = Rectangle(12, 10)

print(f"Dimension of Rectangle - length : {new_Rectangle.length} Width : {new_Rectangle.width}")

print("Area of Rectangle :", new_Rectangle.rectangle_area())

print("Preimeter of Rectangle :", new_Rectangle.rectangle_preimeter())