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

# Property (Decorator) start with _private variable to not let put -negative values later in widht or height
class Rectangel:
    def __init__(self, widht, height):
        self._width = widht
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

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
obj1.width = -100

# Property 2 : We don't use _width or _height private variable so now we can't put negative values in the beginning itsel
# For ex r= Recatangel(-100,10) this will throw value error
# In our above version we could have passed negative values initally i.e  r= (-100,10) but not later
class Rectangel:
    def __init__(self, widht, height):
        self._width = widht
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

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
obj1.width = -100