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
    combine = False
    if i < len(nums):
        combined_num = int(str(curr) + nums[i])
        combine = isValid(nums, res, i + 1, combined_num) 
    return isValid(nums, res, i+1, mult) or isValid(nums, res, i+1, add) or combine

# print(isValid(["6", "8", "6", "15"], 7290, 0, 0))
# print(isValid(["6", "8"], 68, 0, 0))

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
