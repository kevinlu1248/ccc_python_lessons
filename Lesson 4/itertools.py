# demonstration of commonly used tools in itertools
# commonly used ones from https://docs.python.org/2/library/itertools.html#module-itertools
# do not memorize them but just remember they exist when you practice
# 

from itertools import *

# for repetition

# count
for i in count():
     if i == 10:
          break
     print(i)

# cycle
n = 0
for i in cycle('ABCD'):
     print(i)
     n += 1
     if n > 8:
          break

# repeat
for i in repeat('X', 3):
     print(i)

# combinatorical functions

# fun fact: the reason it is called a product is since this is precisely what you would arrive
# at if you expanded (A + B + C)(X + Y + Z)
print(list(product('ABC', 'XYZ')))

print(list(permutations('ABCD', 2)))

print(list(combinations('ABCD', 2)))

# for iterators

print(list(starmap(lambda a, b: a > b, [(1,2), (4,5), (10, 1)])))

# HW #1: find out what tee() does from https://docs.python.org/3/library/itertools.html#itertools.tee 

# functools: https://docs.python.org/3/library/functools.html
# operators: https://docs.python.org/3/library/operator.html
