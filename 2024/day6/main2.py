from pathlib import Path
import sys

sys.setrecursionlimit(10000)
input = Path("input2")

lines = [line.rstrip("\n") for line in input.read_text().splitlines()]

grid = [list(row) for row in lines]

start_i, start_j = 0, 0
m, n = len(grid), len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j] == '^':
            start_i, start_j = i, j

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)
order = [up, right, down, left]

def traverse(i, j, order_idx):
    if i < 0 or j < 0 or i >= m or j >= n:
        return
    i_diff, j_diff = order[order_idx]
    grid[i][j] = 'X'
    next_i, next_j = i + i_diff, j + j_diff
    if next_i >= 0 and next_j >= 0 and next_i < m and next_j < n and grid[next_i][next_j] == '#':
        order_idx += 1
        order_idx %= 4
        i_diff, j_diff = order[order_idx]
    else:
        i += i_diff
        j += j_diff
    traverse(i, j, order_idx)

def isValid(i, j, order_idx, visited):
    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    i_diff, j_diff = order[order_idx]
    next_i, next_j = i + i_diff, j + j_diff
    if (i, j, i_diff, j_diff) in visited:
        return True
    visited.add((i, j, i_diff, j_diff))
    if next_i >= 0 and next_j >= 0 and next_i < m and next_j < n and grid[next_i][next_j] == '#':
        order_idx += 1
        order_idx %= 4
        i_diff, j_diff = order[order_idx]
    else:
        i += i_diff
        j += j_diff

    return isValid(i, j, order_idx, visited)
    
    

traverse(start_i, start_j, 0)
grid[start_i][start_j] = '.'
count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'X':
            grid[i][j] = '#'
            if isValid(start_i, start_j, 0, set()):
                count += 1
            grid[i][j] = 'X'

print(f"COUNT: {count}")


