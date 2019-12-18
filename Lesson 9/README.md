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
    * How little resources an algorithm uses
* Big O, Big Theta, Big Omega
    * Used to measure efficiency and uses asymptotic notation
* Asymptotic Notation
    * How to functions compare for very large values of its inputs
* Data structures
    * Stacks
        * First in last out
        * Push pop and peak are constant time
    * Queue
        * First in first out
        * Push pop and peak are constant time
    * Deque
        * Double ended queue
    * Array Lists
        * More or less just lists
        * Constant everything except insertion, deletion and traversing
    * Linked Lists
        * Train analogy
        * Constant everything except accessing and traversing
    * Sets
        * Unordered dataset
        * Everything only appears once
        * Constant time for checking for membership
    * Dictionary
        * Key value pairs
        * Everything is hashed and checking things is constant time
    * ```collections```
        * ```namedTuple()``` 
            * Immutable dictionary
        * ```Counter```
            * Dictionary with only numbers for values
            * Great for counting things, thus the name
        * ```defaultdict```
            * Dictionary with default value
