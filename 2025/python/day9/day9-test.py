import math

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2)+1) * (abs(y1-y2) + 1)

        
    # only valid if only one wall is empty

# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    lines = f.readlines()

arr = []
# grid = [['.'] * 13 for _ in range(9)]
grid = [['.'] * 100000 for _ in range(100000)]

max_x = 0
max_y = 0
for line in lines:
    x, y = line.strip().split(',')
    num_i, num_j= int(y), int(x)
    grid[num_i][num_j] = '#'
    max_x = max(max_x, num_i)
    max_y = max(max_y, num_j)
    arr.append((int(x), int(y)))
# print(grid)


for i in range(0, len(arr)):
    if i == 0:
        prev_x, prev_y = arr[len(arr) - 1]
    else:
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

# print("-------")
# print(grid)
# print("--------")

for i in range(len(grid)):
    fill = False
    for j in range(len(grid[0])):
        curr = grid[i][j]
        if fill and curr == '.':
            grid[i][j] = 'X'
            continue
        if curr == 'X':
            fill = not fill
            continue
        flag = False
        while j < len(grid[0]) and (curr == 'X' or curr == '#'):
            curr = grid[i][j]
            fill = False
            flag = True
            j += 1
        if flag:
            for temp_j in range(j, len(grid[0])):
                if grid[i][temp_j] == 'X':
                    fill = True
                    j -= 1

# print(grid)

def isValid(p1, p2, grid):
    i1, i2 = p1[1], p2[1]
    j1, j2 = p1[0], p2[0]

    min_i, max_i = min(i1, i2), max(i1, i2)
    min_j, max_j = min(j1, j2), max(j1, j2)

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            curr = grid[i][j]
            if curr == '.':
                return False
    return True


largest_area = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        curr_area = area(arr[i], arr[j])
        if curr_area < largest_area:
            continue
        if isValid(arr[i], arr[j], grid):
            largest_area = max(largest_area, area(arr[i], arr[j]))

print(largest_area)

