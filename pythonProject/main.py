class Shape:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def save(self, file):
        shape_data = f"{self.__class__.__name__},{','.join(f'{k}:{v}' for k, v in self.__dict__.items())}\n"
        with open(file, 'a') as f:
            f.write(shape_data)


class Square(Shape):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def show(self):
        print(f"Čtverec - souřadice horního rohu: {self.x}, {self.y} a délka strany je: {self.length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Obdélník - souřadice horního rohu: {self.x}, {self.y}, délka: {self.width} a šířka: {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Kruh - souřadice: {self.x}, {self.y} a radius je: {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Elipsa - souřadice horního rohu: {self.x}, {self.y}, délka: {self.width} a šířka: {self.height}")

shapes = []
s = Square(0, 0, 10)
r = Rectangle(0, 0,10, 20)
c = Circle(2, 8,10)
e = Ellipse(5,6,50, 20)


file_path = 'shapes.txt'
for shape in shapes:
    shape.save(file_path)


s.show()
r.show()
c.show()
e.show()