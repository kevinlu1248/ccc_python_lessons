# https://dmoj.ca/problem/ccc18j5
# Choose your own path

'''
Sample Input 1
Copy

3
2 2 3
0
0

Sample Output 1
Copy

Y
2

Explanation for Sample Output 1

Since we start on page 1 1 , and can reach both page 2 2 and page 3 3 , all pages are reachable. The only paths in the book are 1 → 2 1 \rightarrow 2 and 1 → 3 1 \rightarrow 3 , each of which is 2 2 pages in length.
Sample Input 2
Copy

3
2 2 3
0
1 1

Sample Output 2
Copy

Y
2
'''

from queue import Queue

# inputting

N = int(input())
book = [[] for _ in range(10010)] # directed unweighted graph
endpoints = set() # all ending points
start = None # starting page

for i in range(1, N + 1):
    n, *arr = map(int, input().split())
    if n == 0:
        endpoints.add(i)
    else:
        if not start: start = i
        book[i] = arr
    # print(n, arr)

# processing 

# checking if every page traversable
traversed = [False for i in range(10010)]

# dfs (O(N))
def dfs(page):
    traversed[page] = True
    for i in book[page]:
        if not traversed[i]: dfs(i)
dfs(start)

# find shortest path
visited = set()

# bfs (no recursion required) (O(N))
def bfs():
    q = Queue(N + 10)
    q.put((start, 0)) # (page, length)
    while not q.empty():
        page, length = q.get()
        if page in visited: continue
        visited.add(page)
        for new_page in book[page]:
            if new_page in endpoints: return length + 2
            q.put((new_page, length + 1))

# outputting

print('Y' if all(traversed[1: N + 1]) else 'N')
print(bfs())