## Review
### Summary
* Python
    * Zip
    * Input methods
    * List comprehension and map
    * Lambda
    * Itertools
* Computer Science
    * Algorithm
    * Efficiency (Big O, Big Theta, Big Omega)
    * Data structures
        * Stacks
        * Queues
        * Array Lists
        * Linked Lists
        * Sets
        * Dictionary
        * Collections
            * ```namedTuple()``` 
            * ```Counter```
            * ```defaultdict```

### Python
* Zip => flips the rows and columns
* Input methods
```python
# using list comprehension
grid = []
for _ in range(int(input())):
    grid.append([int(n) for n in input().split()])
# using map
grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))
```
* List comprehension and map
```python
# list comprehension usually looks something like
list_comp = [term for iteration in iterator if condition else other_term]
```
* Lambda
    * More or less a shortcut function
```python
square = lambda x: x ** 2
square(5)
# 25
```
* itertools
    * count
    * cycle
    * repeat
    * product
    * combination
    * permutation
    * starmap
    * compress
    * accumulate
    * zip_longest

#### Computer Science
* Algorithm
    * A set of instructions to complete a certain task
* Efficiency
    * 