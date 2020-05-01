# Return square of a number
lambda x : x**2

# Sum of two numbers
lambda x,y : x + y

# Lambda function with no parameters
lambda : "hello"

# Slicing and upper
lambda s : s[::-1].upper()

# We can assign a lambda function to a variable name
my_func = lambda x : x**2
print(my_func)
print(my_func(5))

# You can pass lambda as argument to a UDF
def my_func(x, fn):
    return fn(x)

print(my_func(10, lambda x: x**2))

# Default parameter
g = lambda x, y=10 : x + y

print(g(10))

f= lambda x, *args, y, **kwargs : (x, args, y, kwargs)
print(f(1, "a", "b", y=100, a=10))


def apply_function(fn, *args, **kwargs):
    return (fn(*args, **kwargs)) # Here we are using *args and **kwargs to unpack tuple and dictionary and then go inside the function

sq = lambda x : x**2

print(apply_function(sq, 5))

print(apply_function(sq, 5))

help(sorted)

l= [1,4,3,8,5]
print(sorted(l))

l= ["c", "B", "D", "a"]
print(sorted(l)) # Here since capital letter words are arranged on lower number they get sorted first and then small letters

# Now to get rid off the capital letter problem we will make everything uppercase and then sort
print(sorted(l, key= lambda x: x.upper()))

d = {"def": 300, "abc": 200, "ijk": 400}
print(sorted(d))
print(sorted(d, key= lambda x: d[x]))

# d[e], d= dictionary, e= value

# Find distance of imaginary number from origin
def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

print(dist_sq(1+1j))

l= [3,3+3j, 1-1j,0,3]
print(sorted(l, key=dist_sq))

print(sorted(l, key= lambda x : (x.real)**2 + (x.imag)**2))

l= ["cleese", "Idle", "palin", "champman", "gilliam"]

# sort by the last character
print(sorted(l, key= lambda x : x[-1]))

# Randomize an iterable
import random
l= [1,2,3,4,5,6,7,8,9]
print(sorted(l, key= lambda x: random.random()))

# To check functions are callable or not
print(callable(print))
print(callable("abc".upper))

l= [1,2,3,4]
print(callable(l.append))

# Define a method in a class which is callable
class MyClass:
    def __init__(self,x=0):
        print("Initalizing")
        self.counter = x

    def __call__(self, x=1):
        print("updating counter")
        self.counter += x

b= MyClass()
print(b.counter)

MyClass.__call__(b,10)
print(callable(b))