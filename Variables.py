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

