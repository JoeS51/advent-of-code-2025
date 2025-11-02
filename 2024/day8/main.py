input = "input2"

with open(input, 'r') as file:
    lines = file.readlines()

m,n = len(lines), len(lines[0])
grid = [["."] * (n-1) for _ in range(m)]

i = 0
ma = {}
for line in lines:
    j = 0
    for char in line:
        if j == n-1:
            continue

        if char not in ma and char != ".":
            ma[char] = []

        if char != ".":
            ma[char].append((i, j))
        grid[i][j] = char
        j += 1
    i += 1
print(grid)
print(ma)
antinodes = set()
for i in range(m):
    for j in range(n-1):
        char = grid[i][j]
        if char != ".":
            l = ma[char]
            for other_i, other_j in l:
                if i == other_i and j == other_j:
                    continue
                diff_i, diff_j = ((i - other_i) * 1), ((j - other_j) * 1)
                actual_i, actual_j = (i + diff_i), (j + diff_j)
                if 0 <= actual_i < m and 0 <= actual_j < n-1:
                    antinodes.add((actual_i, actual_j))
print(len(antinodes))
                
