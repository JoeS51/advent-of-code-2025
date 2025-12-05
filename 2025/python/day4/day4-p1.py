# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    input = f.readlines()

m = len(input)
n = len(input[0].strip())

grid = [["."] * n for _ in range(m)]
i = 0
for line in input:
    for j in range(n):
        grid[i][j] = line[j]
    i += 1

def can_access(i, j):
    dirs = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
    num_adj_paper = 0
    for x, y in dirs:
        new_i, new_j = i - x, j - y
        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "@":
            num_adj_paper += 1
    return num_adj_paper < 4

total = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            if can_access(i, j):
                total += 1
print(total)

