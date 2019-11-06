## Schedule and Outline
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
This at best would take 1 step, at worst would take n steps, and on average n / 2 steps.

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
In the best case scenario it would take one step, worst case scenario log_2(n) and the average case scenario is somewhere in between (specifically you can find out the exact formula here https://www.wolframalpha.com/input/?i=sigma+from+1+to+infinity&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumlowerlimit%22%7D+-%3E%221%22&assumption=%7B%22C%22%2C+%22sigma%22%7D+-%3E+%7B%22SumWord%22%7D&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumfunction%22%7D+-%3E%22log%28n%2Bx%29%2F2%5Ex%22&assumption=%7B%22F%22%2C+%22Sum%22%2C+%22sumupperlimit2%22%7D+-%3E%22infinity%22). 

So why do we have best case, average case and worst case? Why does it matter and how can we easily quantify and compare them? 

Firstly in terms of definitions, we have big O, big Omega and big Theta notations to describe the amount of time it takes to run an algorithm. In a more formal paper usually they would actually write the greek letters Omega and Theta but for our purposes since I don't know how to type that in into this markdown.