import math
import heapq

# input = "input1"
input = "real-input-1"

with open(input, 'r') as file:
    lines = file.readlines()

dependencies = {}
topo = {}
i = 0
curr_line = lines[i]
while curr_line != '\n':
    nums = curr_line.split("|")
    first_num, second_num = int(nums[0]), int(nums[1][:len(nums[1])-1])
    if first_num not in dependencies:
        dependencies[first_num] = set()
    if second_num not in topo:
        topo[second_num] = []
    topo[second_num].append(first_num)
    dependencies[first_num].add(second_num)
    i += 1
    curr_line = lines[i]
    print("here")

updates = []
i += 1
while i < len(lines):
    curr_line = lines[i]
    print(curr_line)
    nums = curr_line.split(",")
    curr_nums = []
    for j in range(0, len(nums)-1):
        curr = nums[j]
        curr_nums.append(int(curr))
    last_num = int(nums[len(nums)-1][:-1])
    curr_nums.append(last_num)
    updates.append(curr_nums)
    i += 1

def isValid(nums):
    prev_vals = [nums[0]]
    for i in range(1, len(nums)):
        # iterate prev vals and check dependencies
        curr_num = nums[i]
        if curr_num not in dependencies:
            prev_vals.append(curr_num)
            continue
        for prev_val in prev_vals:
            if prev_val in dependencies[curr_num]:
                return False
        prev_vals.append(curr_num)
    return True

def sort_update(nums):
    unique_nums = set(nums)
    q = []
    map = {}
    res = []
    for num in nums:
        map[num] = 0
        if num not in topo:
            heapq.heappush(q, num)
            continue
        for prereq in topo[num]:
            if prereq in unique_nums:
                map[num] += 1
        if map[num] == 0:
            heapq.heappush(q, num)
    while q:
        curr_num = heapq.heappop(q)
        res.append(curr_num)
        if curr_num not in dependencies:
            continue
        for connected in dependencies[curr_num]:
            if connected in map:
                map[connected] -= 1
                if map[connected] == 0:
                    heapq.heappush(q, connected)
    print(update)
    print("---")
    print(res)
    return res[len(res) // 2]
    
sum = 0 
for update in updates:
    if not isValid(update):
        sum += sort_update(update)

print(sum)
