import math

# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    lines = f.readlines()

arr = []

for line in lines:
    x, y = line.strip().split(',')
    arr.append((int(x), int(y)))

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2)+1) * (abs(y1-y2) + 1)

largest_area = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        curr_area = area(arr[i], arr[j])
        largest_area = max(largest_area, curr_area)

print(largest_area)
