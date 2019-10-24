# Lambda Introduction
# Kevin Lu

# WARMUP QUESTION
# take a string of space-seperated integers '1 2 3 4 5' and return every integer squared
# try doing this semi-code-golf: try using less but maintaining clarity

# ANSWER (using list comprehension)
def square(s):
    return ' '.join([str(int(i) ** 2) for i in s.split()])
print(square('1 2 3 4 5'))

# an alternative way to do this is to simply use lambda
def square(s):
    return ' '.join(map(lambda i: str(int(i) ** 2), s.split()))
print(square('1 2 3 4 5'))

# So what is lambda?
# lambda is what's called an anonymous function, which is by definition an unnamed function
# furthermore, it can also be used as a shorthand

# so lets first look a simple usage of it to subsitute a function
# this function squares a string then returns a string
square_string = lambda i: str(int(i) ** 2)
print(square_string('5'))

# the beauty of the implementation arises when you simply don't name it and apply it directly
print((lambda i: str(int(i) ** 2))('5'))

# but can't we just use print(str(int('5') ** 2))?
# it is significantly more practical when used with map, filter and reduce!
# as you've seen earlier, map can be used to iterate the function over the entire iterable
# meanwhile filter does exactly what it sounds like it would do: filter items
# for example suppose you wanted to filter out any negative numbers
# you could simply use the following

print(list(filter(lambda i: i >= 0, [-5, -3, 2, 6])))

# this is equivalent to
output = []
for i in [-5, -3, 2, 6]:
    if i >= 0:
        output.append(i)
print(output)

# the last one is simply reduce, which iteratively sets the first term to the function of the first two terms
# eg the following produces the sum

from functools import reduce
print(reduce((lambda a, b: a + b), [-5, -3, 2, 6]))

# this is equivalent to
sum = 0
for i in [-5, -3, 2, 6]:
    sum += i
print(sum)

# ACTIVITY: make an equivalent product function (there's no builtin product function for this)

# try the following problems:
# https://dmoj.ca/problem/ccc18j3
# https://dmoj.ca/problem/ccc15j3 (really long question)
# https://dmoj.ca/problem/ccc14s2 (hint: use tuples)

# code golf (shortest solution wins!)
# https://dmoj.ca/problem/ccc18j2
# https://dmoj.ca/problem/ccc16j2