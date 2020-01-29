## Miscellaneous

### Agenda
* How to check if an algorithm will pass using asymptotic analysis
* Demonstration for a graph theory problem (2018 J5)
* Recursion

### Update
* Next week will be the last week before the CCC and I will attempt to cover dynamic programming
* However, a few things I would like you to cover by yourself if you get the chance include:
    * Sorting algorithms
    * Minimum spanning tree
    * Shortest path on a graph
    * Harder dynamic programming problems

### How to Check if an Algorithm will Pass using Asymptotic Analysis
* The magic number when it comes to computing is 10^9
* A single computer operation takes approximately a nanosecond (~10^-9 s)
* So the general rule of thumb is if your algorithm takes less or equal to 10^8 operations, your algorithm should pass a time limit of 1 second

Example #1

Variables:
* N at most 10^4
```py
# Your algorithm looks like the following
arr = [int(input()) for i in range(N)]

def search(x):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if (arr[i] + arr[j] + arr[k] == x)
                    return (i, j, k)

print(search(int(input())))

# Will your algorithm pass?
```

Example #2

Variables:
* N at most 10^4
* M at most 10^3
```py
arr = [int(input()) for i in range(N)]
arr = [int(input()) for i in range(M)]

def search(x):
    for i in range(N):
        for j in range(M):
            for k in range(M):
                if (arr[i] + arr[j] + arr[k] == x)
                    return (i, j, k)

print(search(int(input())))

# Will your algorithm pass?
```

### Demonstration of Graph Theory


### Recursion
* Recursion is basically where a function calls on itself
* It usually has a base case and a recursive step (like induction)

```py
# eg.
# fibonacci sequence: (every term is sum of last two terms)
# 1 1 2 3 5 8 13 21 34 55
# lets make this into a function!
def fibonacci(n):
    return 1 if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)
```

However, recursion may not give the most optimized solution. For example this method actually yields exponential time, since the approximate ammount of time to solve for ```fibonacci(n)``` is ```fibonacci(n)```, which approximates to exponential time. Also it uses approximately ```fibonacci(n)``` space too which is also exponential space

```py
# faster method
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n): a, b = b, a + b
    return b
# This is actually linear time (O(n)) and constant space (O(1)).

# Note: the syntax used above is actually really useful (called tuple unwrapping)
# great for swapping two values
x, y = y, x
```

ACTIVITY: Find all anagrams of a string (answer below)

```py
# Note: this is factorial time, space and solution so it is not recommended to try anything above 10 characters (your computer may crash)
def anagrams(s):
    if len(s) == 1: return [s]
    sols = []
    for index, char in enumerate(s):
        if (index != len(s):):
            sols.extend([char + string for string in anagrams(s[:index] + s[index + 1:])])
        else:
            sols.extend([char + string for string in anagrams(s[:index])])
s = "python"
print(anagrams(s))
```

Recursion problems:
* Partition n into k parts
* Find all combinations and/or permutations of a string
* Binary search
* More can be found at https://www.techiedelight.com/recursion-practice-problems-with-solutions/ 
