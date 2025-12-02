with open("actual-input", 'r') as f:
    line = f.readline()

arr = line.split(",")
total_sum = 0
for curr_range in arr:
    first, last = curr_range.split("-")
    first_num, last_num = int(first), int(last)
    print(str(first) + " " + str(last))
    for i in range(first_num, last_num+1):
        n = len(str(i))
        if n % 2 != 0:
            continue
        half = n // 2
        first_half = str(i)[0:half]
        second_half = str(i)[half:]
        if first_half == second_half:
            total_sum += i
        print(first_half)
        print(second_half)
print(total_sum)
