# Write a simple function
def my_func(a,b,c):
    print("a={0}, b={1}, c={2}".format(a,b,c))

my_func(1,2,3)

# Write a default parameter function
def my_func(a,b=10,c=50):
    print("a={0}, b={1}, c={2}".format(a,b,c))

# Just pass a=10 while b and c will take default arguments
my_func(10)

# We can pass different values for b and c and it will overwrite default values 10 and 50
my_func(1,2,3)

# Pass values for a and b, c will be default
my_func(1,2)

# Order of arguments does not matter while calling function
def my_func(a,b=10,c=50):
    print("a={0}, b={1}, c={2}".format(a,b,c))

my_func(c=10, a=1, b=100)

# Upacking
l= [1,2,3,4,5,6]
a= l[0]
b= l[1:]
print(a)
print(b)

a,b = l[0], l[1:]
print(a)
print(b)

a,*b = l
print(a)
print(b)

s= "python"
a, *b = s
print(a)
print(b)

t= (1,2,3)
a,*b = t
print(a)
print(b)

[a,b,c]= "XYX"
print(a)
print(b)
print(c)

a,b,*c= s
print(a)
print(b)
print(c)

a,b,*c,d = s
print(a)
print(b)
print(c)
print(d)

a,b,c,d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)

l1= [1,2,3]
l2= [4,5,6]
l= [*l1, *l2]
print(l)

l1=[1,2,3]
s= "python"
print(*l1, *s)

# To unpack dictionary we use ** double star because single * only gives key and ** gives both keys and values
d1= {"key1": 5, "key2": 10}
d2= {"key2": 15, "key3": 20}

# This will onlly print keys
print({*d1, *d2})

# This will print both key and values
print({**d1, **d2})

# Nested Unpacking
a,b,e = [1,2,"xyz"]
print(a)
print(b)
print(c)

a,b,(c,d) = [1,2,"xy"]
print(a)
print(b)
print(c)
print(d)
