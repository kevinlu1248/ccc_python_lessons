# This is a brief document introducing map and list comprehension
# This will use https://dmoj.ca/problem/ccc18s2 as an example
# This is what I see people usually do

"""
I like to put the sample inputs and the sample outputs in the file to make it easier to copy paste
I usually do all of them

Sample Input 1

2
1 3
2 9

Sample Output 1

1 3
2 9
"""

N = int(input())
grid = []
for i in range(N):
    inp = input().split()
    list = []
    for num in inp:
        list.append(int(num))
    grid.append(list)

# RECAP: string.split(glue) is a function that splits a string into an array
# The glue is by default ' ', or a space
# Eg. 'this-is-a-string'.split('-') => ['this', 'is', 'a', 'string']
# Eg. 'this is a string'.split() => ['this', 'is', 'a', 'string']

# Firstly, I like naming variables but I feel like defining N and inp is unnecessary
# You can simplify it to

grid = []
for _ in range(int(input())):
    list = []
    for num in input().split():
        list.append(int(num))
    grid.append(list)

# But how can we take it from here?
# We have two options- list comprehension and map

# Let's start with list comprehension
# Try to understand this by reading it; this is an essential skill of coding

grid = []
for _ in range(int(input())):
    grid.append([int(n) for n in input().split()])

# Secondly, lets look at using map

grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))

# Now lets try implementing this into your solutions for https://dmoj.ca/problem/ccc18s2 and https://dmoj.ca/problem/ccc16j2
