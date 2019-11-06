## Lesson
### Algorithms
* A set of instructions to complete a certain task
* Usually via manipulating with data structures
* Eg. sorting, reversing or scrambling an array are all examples of algorithms
### Efficiency
Some algorithms are faster than others. For example, consider linear search and binary search. 

Suppose you have a sorted array and would like to find the index of a specific term.
```python
arr = [1, 2, 3, 4, 5]
def search(n, arr):
    pass
```
Linear search involves checking every term in order to check if they are equivalent to what is being searched for like so:
```python
def search(n, arr):
    for i, v in enumerate(arr):
        if v == n:
            return i
    return None
```
If n is the length of the array, this at best would take 1 step, at worst would take n steps, and on average n / 2 steps.

Binary searching involves recursively checking the middle term and using whether it is bigger or smaller than the value to determine where to search next. If the checked value is equal, were done. If the checked value is greater, then it checks the second half of the like so:
```python
def search(n, arr):
    if arr:
        l = length(arr)
        if n == arr[l // 2]:
            return l // 2
        elif n > arr[l // 2]:
            return l // 2 + search(n, arr[l // 2:]) - 1
        elif n < arr[l // 2]:
            return search(n, arr[:l // 2])
    return None
```
If n is the length of the array, in the best case scenario it would take one step, worst case scenario log_2(n) and the average case scenario is somewhere in between (specifically you can find out the exact formula here https://www.wolframalpha.com/input/?i=sigma+from+1+to+infinity&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumlowerlimit%22%7D+-%3E%221%22&assumption=%7B%22C%22%2C+%22sigma%22%7D+-%3E+%7B%22SumWord%22%7D&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumfunction%22%7D+-%3E%22log%28n%2Bx%29%2F2%5Ex%22&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumupperlimit2%22%7D+-%3E%22infinity%22). 

So why do we have best case, average case and worst case? Why does it matter and how can we easily quantify and compare them? 

### Big O, Big Omega and Big Theta

Firstly in terms of definitions, we have Big O, Big Omega and Big Theta notations to describe the amount of time it takes to run an algorithm. In a more formal paper usually they would actually write the greek letters Omega and Theta but for our purposes I will simply use Omega and Theta in latin letters since I don't know how to type that in into this markdown.

In a nutshell, Big O defines the amount of time (also may be memory or other resources) taken to run an algorithm in the worst case scenario, with respect to the size of the input. For example, the worst case amount of time taken for a linear search is n, so we can say that linear search has time complexity of O(n).

We can define Big Theta and Big Omega similarly for the times in the average and best cases. For example, for a linear search, we have that the time complexities are also Theta(n/2) and Omega(n).

Furthermore, when we compare these times we use whats called an asymptotic notation--we compare its growths as they approach infinity and ignore the coefficients and constants in between, as well as anything smaller. For example, Theta(n/2) is equivalent to Theta(n). More generally, we have O(a * f(n) + b) is equivalent to O(f(n)). This is a relatively informal definition, but simply the concept is adequate for the next few topics we're going to discuss. 

Lastly, the following describes a brief order of the growth of functions:

1 < log(n) < sqrt(n) < n < nlog(n) < n * sqrt(n) < n^2 < n^3 ... < a^n < n!

(note that log(n) are the same regardless of the log base due to the change of base formula producing some constant)

### Activity
Find the Big O, Big Omega and Big Theta times of the following algorithms: (going from easier to harder)
1. (Printing) Given a string of length n, print every letter of the string letter by letter.
2. (Reverse String) Given a string of length n, reverse the string character by character.
3. (Filter String) Given a set of m characters, filter any characters of the set from a string of n characters.
4. (Insertion Sort) Given an array of length n, place the first element in and iteratively place the another element in using a linear sort to find the index.
5. (One of the Worst Sorts Ever) Given an array of length n, iteratively randomly shuffle the array until you get a completely sorted array.
6. (Zipping a Matrix) Given a matrix of dimensions n * m, iteratively take a row and make it into a column.
7. (Brute Force Sudoku) Given an n by n matrix, and having k numbers given, randomly guess the remaining of the Sudoku until you get a correct solution.