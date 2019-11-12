## Lesson on Stacks and Queues
### Introduction on How a Computer Operates
* Storage vs Memory
* Analagous to a workspace
* The desk is the memory and the shelf is the storage
    * To get something from your desk its quick and right in front of you 
    * To get something from your shelf its slow and tedious
    * However, your shelf can store significantly more and your desk is usually wiped clean at the end of the day
* Analagously, memory is quick to retrieve from and storage is slow to access
* However storage can store more and memory can not store anything once the power is off
* Specifically, reading and writing to a specific area of the shelf is usually around linear time while accessing the memory is constant time
    * This is why its called the **Random** Access Memory
    * The only thing you need to retrieve something from the RAM is the address

### Stacks
* This is most likely the simplest **abstract data type** (ADT)
* Imagine this as a stack of plates with a description written on every one of them
    * This is called First In Last Out (FILO)
* Only three operations: pop, push and peak, all of which are constant time 
* Popping returns the top-most plate as well as removes it from the stack
* Pushing puts something on the top of the stack 
* Peaking returns the top item but does not remove it from the top (essentially popping then pushing is back)
* Pro: fast at reading and writing things at the top of the stack
* Cons: Slow at reading and writing anything in the middle of the stack and at the beginning of the stack
* In theory:
    * It starts at a given index, call this index i
    * On push, increment i by 1 and push the item at the given element
    * On pop, decrement i by 1 and delete the item and return it
    * On peak, simply ignore i and return the last element

```python
# Simple implementation of a stack (practical idea not what it theoretically actually is)

class Stack:

    def __init__(self):
        self.list = []
        self.length = 0 # this is kinda optional
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()
    def peak(self):
        if self.length > 0:
            return self.list[-1]
        return None

```

In Python, this is more or less just a list

Practice problem: https://dmoj.ca/problem/ccc13s2

### Queue
* Also likely the simplest ADT
* Imagine a lineup at a concession stand
    * Only the front most person can leave the line and you can only leave through the back of the line
    * This is called First In First Out (FIFO)
* Also only three operations: pop, push and peak, all of which are constant time 
* Popping returns the front-most person in the line as well as removes the person from the line
* Pushing puts someone at the back of the line
* Peaking returns the front-most person but does not remove them (essentially popping then pushing is back)
* Pro: fast at reading things at the front of the queue and putting things at the back
    * This is crucial for BFS as you will see later on
    * For example: suppose you want to capitalize every name in a file directory only with a specified depth, this can be done with a queue
* Cons: Slow at almost everything else, including reading things
* In theory:
    * It starts with given starting and ending indexes, call these i and j respectively
    * On push, increment j by 1 and push the item at the given index
    * On pop, increment i by 1, delete the first item and return it
    * On peak, simply ignore i and j and return the last element

```python
# Simple implementation of a stack (practical idea not what it theoretically actually is)

class Queue:

    def __init__(self):
        self.list = []
        self.length = 0 # this is kinda optional
    def push(self, item):
        self.list.insert(0, item)
    def pop(self):
        return self.list.pop()
    def peak(self):
        if self.length > 0:
            return self.list[-1]
        return None

```

In Python, this is builtin by running the following
```python
from collections import deque
```

DEQue is actually a **double ended queue** which basically pops and pushes both from the front and back at constant time, which is adequate for purposes needed for queues.

Though the time complexity makes it seem like DEQue is really fast however its a few times slower if you simply need a stack or a queue.

Furthermore, ```collections``` as a library actually provides a lot more as you will see later on.

Practice problem: https://dmoj.ca/problem/ccc13s2