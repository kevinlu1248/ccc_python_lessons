# Just a quick review
# conditionals, loops, and function

# If elif else statements

age = 16
if age >= 18:
    print("You are an adult")
elif age < 18:
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