#file = "input2.txt"
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

def check(char1, char2):
    if (char1 != 'M' and char1 != 'S') or (char2 != 'M' and char2 != 'S'):
        return False
    if not((char1 == 'M' and char2 == 'S') or (char1 == 'S' and char2 == 'M')):
        return False
    return True


def is_valid(i: int, j: int):
    # check that top left and bottom right aren't equal
    tl_i, tl_j = (i-1), (j-1)
    br_i, br_j = (i+1), (j+1)
    bl_i, bl_j = (i+1), (j-1)
    tr_i, tr_j = (i-1), (j+1)
    tl_char = board[tl_i][tl_j]
    br_char = board[br_i][br_j]
    tr_char = board[tr_i][tr_j]
    bl_char = board[bl_i][bl_j]
    return check(tl_char, br_char) and check(bl_char, tr_char)

total = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        curr_char = board[i][j]
        # skip non x
        if curr_char != 'A':
            continue
        # go all dir
        if is_valid(i, j):
            total += 1

print("TOTAL: " + str(total))


