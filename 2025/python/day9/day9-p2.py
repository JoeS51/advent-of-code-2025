import math

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2)+1) * (abs(y1-y2) + 1)

        
    # only valid if only one wall is empty

# with open("sample-input", 'r') as f:
with open("sample-input", 'r') as f:
    lines = f.readlines()

arr = []
grid = [['.'] * 13 for _ in range(9)]

for line in lines:
    x, y = line.strip().split(',')
    num_i, num_j= int(y), int(x)
    grid[num_i][num_j] = '#'
    arr.append((int(x), int(y)))

print(grid)

for i in range(1, len(arr)):
    prev_x, prev_y = arr[i-1]
    curr_x, curr_y = arr[i]
    min_x, max_x = min(prev_x, curr_x), max(prev_x, curr_x)
    min_y, max_y = min(prev_y, curr_y), max(prev_y, curr_y)

    if min_x == max_x:
        for i in range(min_y + 1, max_y):
            grid[i][max_x] = 'X'
    else:
        for j in range(min_x + 1, max_x):
            grid[max_y][j] = 'X'

def isValid(p1, p2, grid):
    j1, i1 = p1
    j2, i2 = p2
    if j1 == j2 or i1 == i2:
        return False
    min_i, max_i = min(i1, i2), max(i1, i2)
    min_j, max_j = min(j1, j2), max(j1, j2)

    count = 0
    for i in range(min_i, max_i+1):
        curr = grid[i][j1]
        if curr == '.':
            while i < len(grid) and grid[i][j1] == '.':
                i += 1
            if i >= len(grid):
                count += 1
            break

    for i in range(min_i, max_i+1):
        curr = grid[i][j2]
        if curr == '.':
            while i < len(grid) and grid[i][j2] == '.':
                i += 1
            if i >= len(grid):
                count += 1
            break
    for j in range(min_j, max_j+1):
        curr = grid[i1][j]
        if curr == '.':
            while j < len(grid[0]) and grid[i1][j] == '.':
                j += 1
            if j >= len(grid):
                count += 1
            break
    for j in range(min_j, max_j+1):
        curr = grid[i2][j]
        if curr == '.':
            while j < len(grid[0]) and grid[i2][j] == '.':
                j += 1
            if j >= len(grid):
                count += 1
            break
    print(p1)
    print(p2)
    print(count)
    print(area(p1, p2))
    print("-------")

    return count <= 1

print("-------")
print(grid)

largest_area = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if isValid(arr[i], arr[j], grid):
            largest_area = max(largest_area, area(arr[i], arr[j]))

print(largest_area)


