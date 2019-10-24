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
test
