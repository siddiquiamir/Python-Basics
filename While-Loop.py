# Simple while loop
i = 0
while i < 5:
    i+= 1
    print(i)

# Print only 5
i = 5
while True:
    if i >= 5:
        print(i)
        break

# Break Statement (put increment below break statement)
i= 0
while i < 10:
    print(i)
    if i ==5:
        break
    i+=1

# Continue Statement
i=0
while i < 10:
    i+=1
    if i%2==0:
        continue
    print(i)

# Else statement in while
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

# Example
count = 0
while count < 3:
    count+=1
    print("Hello", count)

# Print only if length of name is greater than 2
num_digits = 2
while True:
    name = input("Please enter your name: ")
    if len(name) >= num_digits and name.isprintable() and name.isalpha():
        break
print("Hello {}".format(name))

# Check if number already exists otherwise insert that number in the list
l = [10,20,30,40,50]
print(l)
num = 5
index = 0
while index < len(l):
    if l[index]== num:
        break
    index+= 1
l.append(num)
print(l)

# Try and Except
a= 10
b= 0

try:
    a/b
except ZeroDivisionError:
    print("Number divided by zero")

# Try and Except while loop
a= 0
b= 3

while a < 5:

    a+=1
    b-=1
    try:
        a/b
    except ZeroDivisionError:
        print("Number divided by zero")
    finally:
        print("This line always print")

# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print('Current Letter :', a[i])
    i += 1

# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass
print('Value of i :', i)

# Python program to demonstrate
# while-else loop
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")