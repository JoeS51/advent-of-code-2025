import math
input = "input1"

with open(input, 'r') as f:
    lines = f.readlines();

curr_point = 50
sum = 0
prev = False
for curr_line in lines:
    if curr_line[0] == "L":
        dir = -1
    else:
        dir = 1
    rot = int(curr_line[1:])
    prev_point = curr_point
    curr_point += (dir * rot)
    curr_point %= 100
    if curr_point == 0:
        sum += 1
print(sum)

