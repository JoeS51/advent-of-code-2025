file = "input"

with open(file, 'r') as file:
    lines = file.readlines()

m = len(lines)
n = len(lines[0])

board = [[''] * n for _ in range(m)]

i = 0
for line in lines:
    j = 0
    for char in line:
        #if j == n:
        #    continue
        board[i][j] = char
        j += 1
    i += 1
chars = ['X', 'M', 'A', 'S']

def dir(i, j, i_off, j_off, next_i):
    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    if board[i][j] != chars[next_i]:
        return False
    if next_i == len(chars) - 1:
        return True
    return dir(i + i_off, j + j_off, i_off, j_off, next_i+1)

total = 0
for i in range(m):
    for j in range(n):
        curr_char = board[i][j]
        # skip non x
        if curr_char != 'X':
            continue
        # go all dir
        before = total
        total += dir(i, j, 1, 0, 0) 
        total += dir(i, j, -1, 0, 0)
        total += dir(i, j, 0, 1, 0)
        total += dir(i, j, 0, -1, 0)
        total += dir(i, j, 1, 1, 0)
        total += dir(i, j, -1, 1, 0)
        total += dir(i, j, 1, -1, 0)
        if i == 9 and j == 3:
            print("HERERE")
            print(total)
        total += dir(i, j, -1, -1, 0)
        if i == 9 and j == 3:
            print(total)
        after = total
        if after > before:
            print(str(i) + " " + str(j))
            print(after - before)

print("TOTAL: " + str(total))


