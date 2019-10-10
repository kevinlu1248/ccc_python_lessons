# https://dmoj.ca/problem/ccc18s2
# Kevin Lu

grid = [[int(n) for n in input().split()] for _ in range(int(input()))]
FIX_HORI = grid[0][0] > grid[0][1]
FIX_VERT = grid[0][0] > grid[1][0]

if FIX_HORI and FIX_VERT:
    grid = [row[::-1] for row in grid[::-1]]
elif not FIX_HORI and FIX_VERT:
    grid = [row for row in grid[::-1]]
elif FIX_HORI and not FIX_VERT:
    grid = [row[::-1] for row in grid]

[print(' '.join(map(str, row))) for row in grid]

"""
Sample Input 1
Copy

2
1 3
2 9

Sample Output 1
Copy

1 3
2 9

Sample Input 2
Copy

3
4 3 1
6 5 2
9 7 3

Sample Output 2
Copy

1 2 3
3 5 7
4 6 9

Sample Input 3
Copy

3
3 7 9
2 5 6
1 3 4

Sample Output 3
Copy

1 2 3
3 5 7
4 6 9
"""
