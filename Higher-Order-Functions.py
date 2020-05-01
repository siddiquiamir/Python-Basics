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