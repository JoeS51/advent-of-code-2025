from functools import lru_cache
# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    input = f.readlines()

grid = [list(row.strip()) for row in input]
m = len(grid)
n = len(grid[0])
q = []

initial_j = 0
# find 'S' position first and add first beam below it
for i in range(n):
    if grid[0][i] == 'S':
        initial_j = i
        q.append((1, i))
        break

visited = set()

# BFS
while q:
    q_len = len(q)
    for i in range(0, q_len):
        curr_i, curr_j = q.pop(0)
        if 0 <= curr_i < m and 0 <= curr_j < n:
            curr_symbol = grid[curr_i][curr_j]
            if curr_symbol == '.':
                grid[curr_i][curr_j] = '|'
                if (curr_i + 1, curr_j) not in visited:
                    visited.add((curr_i + 1, curr_j))
                    q.append((curr_i+1, curr_j))
            else: # case that beam is split
                if (curr_i, curr_j + 1) not in visited:
                    visited.add((curr_i, curr_j + 1))
                    q.append((curr_i, curr_j + 1))
                if (curr_i, curr_j - 1) not in visited:
                    visited.add((curr_i, curr_j - 1))
                    q.append((curr_i, curr_j - 1))
print(grid)

@lru_cache(maxsize=None)
def dfs(i, j):
    if 0 <= i < m and 0 <= j < n:
        if i == m-1 and grid[i][j] == '|':
            return 1
        if grid[i][j] == '^':
            return dfs(i, j+1) + dfs(i, j-1)
        elif grid[i][j] == '|':
            return dfs(i+1, j)
        else:
            return 0

res = dfs(1, initial_j)
print(res)
