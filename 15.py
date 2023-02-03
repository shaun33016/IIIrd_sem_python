class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


n = int(input("Enter the number of rectangles: "))
rectangles = []

for i in range(n):
    width = int(input("Enter the width of rectangle {}: ".format(i + 1)))
    height = int(input("Enter the height of rectangle {}: ".format(i + 1)))
    rectangles.append(Rectangle(width, height))

max_area = 0
min_area = float('inf')
max_rectangle = None
min_rectangle = None

for rectangle in rectangles:
    if rectangle.getArea() > max_area:
        max_area = rectangle.getArea()
        max_rectangle = rectangle
    if rectangle.getArea() < min_area:
        min_area = rectangle.getArea()
        min_rectangle = rectangle

print("Rectangle with maximum area:")
print("Width:", max_rectangle.width)
print("Height:", max_rectangle.height)

print("Rectangle with minimum area:")
print("Width:", min_rectangle.width)
print("Height:", min_rectangle.height)
