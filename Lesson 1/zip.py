# in python we have multi-dimensional arrays (aka matrices)

# eg.
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# suppose you want to rotate this to the following
# ie. its column becomes its rows and vice versa

desired_array = [[1, 4, 7],
                 [2, 5, 8],
                 [3, 6, 9]]

# there's a function that does this perfectly!
# zip accomplishes exactly this: it makes its rows its columns and its columns its rows

zipped_array = zip(*array)

for row in zipped_array: # notice how you can do this because zip objects are iterables!
    print(row)

# NOTE: this is a bit off topic but you can also print this using list comprehension or print it by making it a list
# eg.

print(list(desired_array))
# we'll go over the next two another time
print([row for row in desired_array])
[print(row) for row in desired_array]

# ACTIVITY: rotate a matrix 90%
def rotate(matrix):
    return zip(*matrix[::-1])

[print(row) for row in rotate(array)]

# ACTIVITY: do dmoj 2018 j4 using zip at dmoj.ca/problems/ccc18j4
