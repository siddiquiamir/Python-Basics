# Higher Order Functions : A function that takes a function as a parameter and/or returns a function as its return value
# Example Sorted, Map, Filter

l= [1,2,3]

def sq(x):
    return x**2

list(map(sq,l))

l1=[1,2,3]
l2=[10,11,12]

def add(x,y):
    return x+y

list(map(add,l1,l2))

list(map(lambda x,y: x+y, l1,l2))

# Filter : It takes a function and a single iterable only. It will return an iterator that contains all the elements of the iterable for which
# the function called on it is Truthy
# If the function is None, it simply returns the elements of iterable that are truthy.

l=[0,1,2,3,4,5]
list(filter(None,l)) # 0 won't return because it is false

def iseven(x):
    return x%2==0

print(list(filter(iseven,l)))

# For loop
l=[1,2,3,4,5]
result =[]
for i in l:
    result.append(i**2)

print(result)

# List comphrension
print([i**2 for i in l])

# Example of Zip as an alternate to lambda function
print(list(map(lambda x,y: x+y,l1,l2)))

print([i+j for i,j in zip(l1,l2)])

# List Comphrension alternate to filter
print(list(filter(lambda x: x%2==0,l1)))

print([i for i in l if i%2==0])

# List Comphrension and two two higher order function
l= range(10)
print(l)

list(filter(lambda x: x <25,map(lambda x: x**2,l)))

print([i**2 for i in l if i**2 <25])

# Factorial function
def fact(n):
    return 1 if n <2 else n * fact(n-1)

print(fact(5))

def factt(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)
print(factt(5))

results = map(fact, range(10))
print(results)
for i in result:
    print(i)

# Reducing function
l= [5,8,6,10,9]
max_value = lambda x,y : x if x > y else y

def max_sequence(list):
    result= l[0]
    for i in l[1:]:
        result= max_value(result,i)
    return result

print(max_sequence(l))

# Let's do reduce function (Above function is hard code while this not hardcode)
def _reduce(fn, list):
    result= list[0]
    for i in list[1:]:
        result= fn(result,i)
    return result

print(_reduce(max_value,l))

# Adding all the elements in the list
add_func = lambda x,y : x+y
print(_reduce(add_func,l))

# Lets use reduce from python moduel and it is very easy
# Reduce works only on iterable
from functools import reduce
print(reduce(lambda x,y : x+y, l))

print(reduce(lambda x,y : x if x > y else y, l))

print(reduce(lambda x,y : x if x < y else y, l))

print(reduce(lambda a,b : bool(a) or bool(b),l))

print(reduce(lambda x,y : x*y,l))

print(reduce(lambda x,y : x*y, range(1,6)))

# Calculate factorial using reduce method
l=[1,2,3,4]
print(reduce(lambda a,b : a*b,l))

five = range(1,7)
print(reduce(lambda a,b : a*b,five))

# Range: To see values of a range we have to convert it to a list
print(range(6))
print(list(range(6)))

# If we do not want zero and want the last number to be included start with 1 and 1+last number
print(list(range(1,6)))

def facto(n):
    return 1 if n < 2 else n * fact(n-1)

print(facto(5))

# Reduce function has initalizer. So now we do not have to use index value
l= [4,5,8,3]
max_value = lambda x,y : x if x > y else y
# old function without initalizer
def _reduce(fn, list):
    result= list[0]
    for i in list[1:]:
        result= fn(result,i)
    return result
# new function with initalizer (we need to pass an initial value while calcuating 0 if we are doing addition and 1 if we are doing multiplicatin)
def _reduce(fn, list, inital):
    result= inital
    for i in list:
        result= fn(result,i)
    return result

print(_reduce(max_value,l,0))
