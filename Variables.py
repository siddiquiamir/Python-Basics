# Variables in python
my_var = 10
print(id(my_var))
print(hex(id(my_var)))

# Reference count
import sys
a= [1,2,3]
print(id(a))
print(sys.getrefcount(a))

import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

b= a
print(sys.getrefcount(b))
print(ref_count(id(b)))

c= b
print(sys.getrefcount(c))
print(ref_count(id(c)))

# Now if we change c=10 reference count will go down
c= 10

print(sys.getrefcount(a))
print(ref_count(id(a)))

# Tuples
a= [1,2,3]
a.append(4)
print(a)

t= ([1,2], [3,4])
print(t)
print(t[0])
t[0].append(10)
print(t)

# Function returning a function
def square(a):
    return a**a

def cube(a):
    return a**3

def select_function(a):
    if a ==1:
        return square
    else:
        return cube

f= select_function(2)
print(f(2))
print(select_function(2)(3))

# Function as parameter
def execute_function(fn,n):
    return fn(n)

print(execute_function(cube,4))

help(int)
int(True)
int(False)