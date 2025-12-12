from functools import lru_cache
# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    file = f.readlines()

adj_map = {}

for line in file:
    nodes = line.strip().split(':')
    start_node = nodes[0]
    adj_map.setdefault(start_node, [])
    children_arr = adj_map[start_node]
    children = nodes[1].strip().split(' ')
    for child in children:
        children_arr.append(child)

# print(adj_map)

@lru_cache(maxsize=None)
def dfs(curr_node, dac, fft):
    if curr_node == "out":
        if dac and fft:
            return 1
    sum = 0
    if curr_node in adj_map:
        for child in adj_map[curr_node]:
            if child == "fft":
                fft = True
            elif child == "dac":
                dac = True
            sum += dfs(child, dac, fft)
    return sum

total = dfs("svr", False, False)
print(f"total is {total}")






# q = [("you", False, False)]
# total = 0
# while q:
#     curr_node, dac, fft = q.pop(0)
#     if curr_node == "out":
#         if dac and fft:
#             print(f"{total}")
#             total += 1
#         continue
#     if curr_node in adj_map:
#         for child in adj_map[curr_node]:
#             if child == "fft":
#                 fft = True
#             elif child == "dac":
#                 dac = True
#             q.append((child, dac, fft))

