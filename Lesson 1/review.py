# Just a quick review
# string formatting, conditionals, loops, and function

# string formatting
x = 5
print("x is {}".format(x))
print("x is {number}".format(number=x))

# if elif else statements

age = 16
if age >= 18:
    print("You are an adult")
elif 0 < age < 18:
    print("You are a minor")
else:
    print("I don't even know what you are...")

# while and for loops

i = 0
while i < 5:
    print("i = {}".format(i))
    i += 1

# this is equivalent to

for i in range(5): # basically (0, 1, 2, 3, 4)
    print("i = {}".format(i))

# functions

def area(s):
    return s * s

side_length = 5
print("The area of a square of side length {} is {}".format(side_length, area(side_length)))