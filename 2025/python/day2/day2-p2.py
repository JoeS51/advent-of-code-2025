with open("actual-input", 'r') as f:
    line = f.readline()

arr = line.split(",")
total_sum = 0
valid = []
for curr_range in arr:
    first, last = curr_range.split("-")
    first_num, last_num = int(first), int(last)
    # print(str(first) + " " + str(last))
    for i in range(first_num, last_num+1):
        n = len(str(i))
        # print("START")
        # print(i)
        for pattern in range(1, (n//2)+1):
            # print("PATTERN")
            curr_range = str(i)[0:pattern]
            # print(curr_range)
            matches = True
            j = pattern
            while matches:
                if j + pattern > len(str(i)):
                    matches = False
                    continue
                next_range = str(i)[j:j+pattern]
                # print("---")
                # print(curr_range)
                # print(next_range)
                # print("---")
                if next_range != curr_range:
                    matches = False
                else:
                    if j + pattern == len(str(i)):
                        # print("JKDLSAJDKLAS:JDKL:ASJDASKLJ")
                        break
                    j += pattern
            if matches:
                total_sum += i
                valid.append(i)
                break
                # print("HERERERE")
                # print(i)
print(total_sum)
print(valid)
