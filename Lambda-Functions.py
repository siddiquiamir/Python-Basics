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

lambda x,*,y : x+y,1,y=20
