with open("actual-input", 'r') as f:
    input = f.readlines()

grid = [list(row.strip()) for row in input]
m = len(grid)
n = len(grid[0])
q = []

# find 'S' position first and add first beam below it
for i in range(n):
    if grid[0][i] == 'S':
        q.append((1, i))
        break

total = 0
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
                total += 1
                if (curr_i, curr_j + 1) not in visited:
                    visited.add((curr_i, curr_j + 1))
                    q.append((curr_i, curr_j + 1))
                if (curr_i, curr_j - 1) not in visited:
                    visited.add((curr_i, curr_j - 1))
                    q.append((curr_i, curr_j - 1))
print(grid)
print(total)

