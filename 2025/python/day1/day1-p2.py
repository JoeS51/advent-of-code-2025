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
    print("0-----")
    print(curr_point)
    print(sum)
    if curr_point > prev_point:
        for i in range(prev_point+1, curr_point+1):
            if i == 0 or (i % 100 == 0):
                sum += 1
    else:
        for i in range(prev_point-1, curr_point-1, -1):
            if i == 0 or (i % 100 == 0):
                sum += 1
    print(sum)
    curr_point %= 100
print(sum)

