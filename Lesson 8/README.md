## Dictionaries and ```collections```
### Dictionaries
* Dictionaries are exactly what it sounds like: a data structure that has a "term" and a "definition"
    * The "term" is usually called a "key" and a "definition" is usually called a "value"
* Furthermore, the key can be of any type (however in Python it must be immutable) and values can also be of any type
* Although slightly slow, this is a really simple and effective data structure in Python
* You can access and insert delete keys and values
```python
# basic dictionary syntax
new_dict = {}
defined_dict = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

# change a key:
defined_dict['a'] = -1

# adding a key:
defined_dict['y'] = 5

# deleting a key:
del defined_dict['y']
```

### ```collections```
We have a few built-in Python data structures:
* namedtuple()
* deque
* ChainMap
* Counter
* OrderedDict
* defaultdict
* UserDict
* UserList
* UserString

But we will only be going over
* namedtuple()
* Counter
* defaultdict

Since everything else is not commonly used in the CCC and deque has already been discussed.

#### ```namedtuple()```
* basically immutable dictionary
```python
# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22)
# 33
x, y = p                # unpack like a regular tuple
x, y
# (11, 22)
p.x + p.y               # fields also accessible by name
# 33
p                       # readable __repr__ with a name=value style
# Point(x=11, y=22)

# source: https://docs.python.org/3.5/library/collections.html#collections.namedtuple
```

#### ```Counter```
* Two interpretations of this
    * Dictionary with only integers as values
    * Multiset
* Very effective for finding the most frequent values of an iterable

```python
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

c = Counter(['eggs', 'ham'])
c['bacon'] 
# output: 0

# source: https://docs.python.org/3.5/library/collections.html#collections.Counter
```

#### ```defaultdict```
* In my opinion the most useful out of the three
* However also the hardest to explain
* By default if you were to call a dictionary with an undefined key it would give you ```None```
* However, for defaultdict, it would give you whatever you set the default value to (eg. 0, [] or {})
* However, suppose you would like to append things to values in a dictionary
    * If you used the dictionary, you would have to split it into two cases: if the key value pair exists or doesn't exist
    * If you used the defaultdict, you can set the default value to [] and always append it (so you have only one case)
* This is extremely useful also in graph theory, which will be covered later

```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# source: https://docs.python.org/3.5/library/collections.html#collections.defaultdict
```


Practice problems
* https://dmoj.ca/problem/ccc01s1
* https://dmoj.ca/problem/ccc02s1
* https://dmoj.ca/problem/ccc03s1
* https://dmoj.ca/problem/ccc05s1