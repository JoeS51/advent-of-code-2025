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

print(adj_map)

q = ["you"]
total = 0
while q:
    curr_node = q.pop(0)
    if curr_node == "out":
        total += 1
        continue
    if curr_node in adj_map:
        for child in adj_map[curr_node]:
            q.append(child)

print(f"total is {total}")

