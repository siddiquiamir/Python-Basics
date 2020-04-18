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
