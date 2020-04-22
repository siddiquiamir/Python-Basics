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

# args
# This always return answer in tuple
def func1(a,b,*args):
    print(a)
    print(b)
    print(args)

func1(101,11,12,13,12,14)
func1(1,2,3,4,3,4)

# Write a function using *args to find average
def avg(*args):
    total= sum(args)
    count= len(args)
    return total/count

print("The average is", avg(2,2,4,4))

# Write a function which returns 0 if no number is passed or returns answer if numbers are passed
def avg1(*args):
    total = sum(args)
    count = len(args)
    if count==0:
        return 0
    else:
        return total/count

print(avg1())
print(avg1(2,2,2))

# Short circut.Better way of writing above code.
def avg1(*args):
    total = sum(args)
    count = len(args)
    return count and total/count

print(avg1())
print(avg1(2,2,2))

def avg1(a,*args):
    total = sum(args) + a
    count = len(args) + 1
    return count and total/count

print(avg1(0))
print(avg1(2,2,2))

# upack elements
def func1(a,b,c):
    print(a)
    print(b)
    print(c)

l=[1,2,3]
func1(*l)

# Upack unlimited list using *args
def func1(a,b,c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l=[1,2,3,4,5,6,7]
print(*l)

def func1(a,b,c):
    print(a,b,c)

func1(10,20,30)
func1(1,c=10, b=90) #once you start using arguments name you have to continue using you can't stop

# Mandatory positinal arguments
def func(a,b,*args,d):
    print(a,b,args,d)

func(2,3,4,5,d=10)

def func(*args,d):
    print(args,d)

func(1,2,3,d=10)
func(d=10)

# In this function you cannot pass any argument excpet positional argument d
def func(*,d):
    print(d)

func(d=100)

# This function will only take default values
def func(a,b,*,d):
    print(a,b,d)

func(a=1,b=2,d=10)
func(1,2,d=100)

def func(a,b=10,*args,d):
    print(a,b,args,d)

func(1,2,3,4,d=10)

def func(a,b=10,*args,d,e):
    print(a,b,args,d,e)

func(1,2,3,4,5,d=100,e=200)
func(0, 600, d="good morning", e="python")
func(0, 600,1,2,3, d="good morning", e="python")

# **kwargs (key word arguments)
def func(**kwargs):
    print(kwargs)

func(a=10,b=20,c=30)

def func(*args,**kwargs):
    print(args,kwargs)

func(1,2,3,4,a=10,b=20)

def func(a,b,*,d,**kwargs):
    print(a,b,kwargs)

func(1,2,3,4,a=10,b=20)

