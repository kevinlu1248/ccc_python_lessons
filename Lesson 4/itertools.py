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

print(list(compress('ABCDEF', [1,0,1,0,1,1])))

print(list(accumulate([1,2,3,4,5])))

print(list(zip_longest('ABCD', 'xy', fillvalue='-')))

# HW #1: find out what tee() and groupby() does from https://docs.python.org/3/library/itertools.html#itertools.tee 

# functools: https://docs.python.org/3/library/functools.html
# operators: https://docs.python.org/3/library/operator.html

# HW #2: Finish problems from last day
# HW #3: Read the following Khan Academy Articles https://www.khanacademy.org/computing/computer-science/algorithms#asymptotic-notation
# (try to finihs everything in the chapetr)
