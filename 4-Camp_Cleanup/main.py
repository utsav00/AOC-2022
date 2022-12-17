def process_inputs(file_path):
    with open(file_path, 'r') as f:
        content = f.read().split('\n')
        return [supplies.split(',') for supplies in content]

def part_1(input):
    common = 0
    for assign_1, assign_2 in input:
        x, y = assign_1.split('-')
        a, b = assign_2.split('-')

        x, y, a, b = int(x), int(y), int(a), int(b)

        if (x >= a and y <= b) or (x <= a and y >= b):
            common += 1
        
    return common

def part_2(input):
    overlap = 0
    for assign_1, assign_2 in input:
        x, y  = assign_1.split('-')
        a, b = assign_2.split('-')

        set_1 = set(range(int(x), int(y) + 1))
        set_2 = set(range(int(a), int(b) + 1))

        if set_1.intersection(set_2) or set_2.intersection(set_1):
            overlap += 1
    
    return overlap

if __name__ == '__main__':
    file_path = './4-Camp_Cleanup/input.txt'
    input = process_inputs(file_path)

    print("--Part 1--")
    print(part_1(input))
    
    print("--Part 2--")
    print(part_2(input))