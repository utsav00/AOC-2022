def process_inputs(file_path):
    with open(file_path, 'r') as f:
        return f.read().split('\n')

def part_1(input):
    result = 0

    for racksack in input:
        length = len(racksack)
        first = racksack[:length//2]
        second = racksack[length//2:]

        common = set(first).intersection(second).pop()

        result += get_value(common)
        
    return result

def get_value(common):
    if common >= 'A' and common <= 'Z':
        return ord(common) % 64 + 26
    else:
        return  ord(common) % 96

def part_2(input):
    result = 0

    for first, second, third in zip(*[iter(input)]*3):
        common = set(first).intersection(second).intersection(third).pop()
        result += get_value(common)
    
    return result

if __name__ == '__main__':
    file_path = './3-Rucksack_Reorganization/input.txt'
    input = process_inputs(file_path)

    print("--Part 1--")
    print(part_1(input))
    
    print("--Part 2--")
    print(part_2(input))