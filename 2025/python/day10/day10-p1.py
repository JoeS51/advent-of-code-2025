# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    lines = f.readlines()

def generate_bits_from_diagram(diagram):
    place = 0
    sum = 0
    for i in range(1, len(diagram)-1):
        if diagram[i] == '#':
            sum += pow(2, place)
        place += 1
    return sum

def generate_button_bits(buttons):
    res = []
    for button in buttons:
        unparsed_buttons = button[1:len(button)-1]
        curr_buttons = unparsed_buttons.split(',')
        curr_sum = 0
        for num in curr_buttons:
            curr_sum += pow(2, int(num))
        res.append(curr_sum)
    return res

def get_min_button_presses(start, end, buttons):
    q = [start]
    steps = 0
    visited = set()
    while q:
        q_len = len(q)
        for i in range(q_len):
            curr_num = q.pop(0)
            if curr_num == end:
                return steps
            for button in buttons:
                next_num = curr_num ^ button
                if next_num in visited:
                    continue
                visited.add(next_num)
                q.append(next_num)
        steps += 1

    return -1

res = 0

for line in lines:
    input_arr = line.split(' ')
    diagram = input_arr[0]
    buttons = input_arr[1:len(input_arr)-1]
    diagram_bits = generate_bits_from_diagram(diagram)
    button_bits = generate_button_bits(buttons)
    res += get_min_button_presses(0, diagram_bits, button_bits)

print(res)
