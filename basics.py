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