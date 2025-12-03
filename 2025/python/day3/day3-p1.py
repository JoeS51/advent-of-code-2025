# go from left to right greedily taking the highest digit for the tens place

# with open("sample-input", 'r') as file:
with open("actual-input", 'r') as file:
    lines = file.readlines()

def calculate_largest_joltage(input):
    tens_place, ones_place = 0, 0
    for i in range(0, len(input)):
        curr_dig = int(input[i])
        if curr_dig > tens_place and (i != len(input) - 1):
            tens_place = curr_dig
            ones_place = 0
        elif i == len(input) - 1:
            ones_place = max(ones_place, curr_dig)
        else:
            ones_place = max(ones_place, curr_dig)
    return tens_place * 10 + ones_place

total_jolt = 0
for line in lines:
    largest_jolt = calculate_largest_joltage(line.strip())
    total_jolt += largest_jolt

print(f"total jolt is {total_jolt}")
