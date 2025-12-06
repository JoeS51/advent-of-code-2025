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

def min_bin_search(target, intervals):
    lo, hi = 0, len(intervals)
    while lo < hi:
        mid = (lo+hi) // 2
        if intervals[mid][0] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

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
print(intervals)
merged_intervals = merge_intervals(intervals)
print(merged_intervals)

total = 0
while i < len(input):
    curr_num = int(input[i].strip())
    first_index_less = min_bin_search(curr_num, merged_intervals)
    if first_index_less == -1:
        i += 1
        continue
    interval_start, interval_end = merged_intervals[first_index_less]
    if interval_end >= curr_num:
        total += 1
    i += 1
print(total)

