def process_inputs(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def part_1(input):
    for i in range(4, len(input)):
        start_of_marker = set(input[i-4: i])
        if len(start_of_marker) == 4:
            return i


def part_2(input):
    for i in range(14, len(input)):
        start_of_marker = set(input[i - 14: i])
        if len(start_of_marker) == 14:
            return i


if __name__ == '__main__':
    file_path = './6-Tuning_Trouble/input.txt'
    input = process_inputs(file_path)

    print("--Part 1--")
    print(part_1(input))

    print("--Part 2--")
    print(part_2(input))
