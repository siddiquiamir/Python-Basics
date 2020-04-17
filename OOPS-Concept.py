# Define an empty class
class Rectangel:
    pass

# Define class and it's properties
class Rectangel:
    def __init__(self, width, height):
        self.widht = width
        self.height = height

# Create Object of Class Rectangel
obj = Rectangel(50,100)
print(obj.widht)
print(obj.height)

# Change value of width
obj.height=20
print(obj.height)

# __str__ and __repr__
class Rectangel:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Rectangle: Width= {}, Height = {}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

obj = Rectangel(20,40)
print(str(obj))
print(obj)

# Equality method
class Rectangel:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def __str__(self):
        return "Rectangle: Width= {}, Height = {}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __eq__(self, other):
        return (self.width, self.height) == (self.width, self.height)

obj1 = Rectangel(20,40)
obj2= Rectangel(20,40)
print(obj1==obj2)
print(obj1 == 100)

class Rectangel:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def __str__(self):
        return "Rectangle: Width= {}, Height = {}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangel):
            return (self.width, self.height) == (self.width, self.height)

obj1 = Rectangel(20,40)
obj2= Rectangel(20,40)
print(obj1==obj2)
print(obj1 == 100)

# Less than __lt__
class Rectangel:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle: Width= {}, Height = {}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __lt__(self, other):
        if isinstance(other, Rectangel):
            return self.area() < other.area()


obj1 = Rectangel(20,40)
obj2= Rectangel(80,40)

print(obj1.area())
print(obj2.area())
print(obj1 < obj2)