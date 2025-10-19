input = "input2"

with open(input, 'r') as file:
    lines = file.readlines()

def isValid(nums, res, i, curr):
    if i >= len(nums):
        if curr == res:
            return True
        else:
            return False
    mult = curr * int(nums[i])
    add = curr + int(nums[i])
    return isValid(nums, res, i+1, mult) or isValid(nums, res, i+1, add)

count = 0
for line in lines:
    nums = line.split(" ")
    res = int(nums[0][:-1])
    total = 0
    last = len(nums) - 1
    nums[last] = nums[last][:-1]
    if isValid(nums, res, 1, 0):
        count += res

print(count)
