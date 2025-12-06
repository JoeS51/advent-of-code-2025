# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    input = f.readlines()

def merge_intervals(intervals):
    merged_intervals = []
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        curr_start, curr_end = intervals[i][0], intervals[i][1]
        if curr_start > end:
            merged_intervals.append((start, end))
            start, end = curr_start, curr_end
        else:
            end = max(end, curr_end)
    merged_intervals.append((start, end))
    return merged_intervals

i = 0
intervals = []
while len(input[i]) != 1:
    curr_line = input[i].strip()
    start, end = curr_line.split("-")
    range_start, range_end = int(start), int(end)
    intervals.append((range_start, range_end))
    i += 1
i += 1
intervals.sort()
merged_intervals = merge_intervals(intervals)

total = 0
for start, end in merged_intervals:
    total += (end - start) + 1
print(total)

