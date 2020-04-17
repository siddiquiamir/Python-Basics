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
