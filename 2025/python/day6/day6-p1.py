# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    input = f.readlines()
grid = []
for line in input:
    nums_arr = line.strip().split()
    curr_arr = [] 
    for num in nums_arr:
        curr_arr.append(num)
    grid.append(curr_arr)

m = len(grid) - 1
n = len(grid[0])

totals = []
for j in range(0, n):
    curr_total = 0
    for i in range(0, m):
        operator = grid[m][j]
        curr_num = int(grid[i][j])
        if operator == "*" and i == 0:
            curr_total = 1
        if operator == "*":
            curr_total *= curr_num
        else:
            curr_total += curr_num
    totals.append(curr_total)

print(sum(totals))
     
        
