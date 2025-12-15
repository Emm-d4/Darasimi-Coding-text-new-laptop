class Circle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def circle_area(self):
        return self.length * self.width
        
    def circle_preimeter(self):
        return 2 * (self.length + self.width)
        
new_circle = Circle(12, 10)

print(f"Dimension of Circle - length : {new_circle.length} Width : {new_circle.width}")

print("Area of Circle :", new_circle.circle_area())

print("Preimeter of Circle :", Circle.circle_preimeter())