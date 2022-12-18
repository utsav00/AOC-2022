import re
from typing import List, Tuple, Any


def process_inputs(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        # content = (i.splitlines() for i in f.read().strip('\n').split('\n\n'))
        content = f.read().split('\n\n')
        return content


def parse_instruction(instruction: str) -> tuple[int, int, int]:
    return map(int, re.findall(r'\d+', instruction))


def part_1(stacks: List[List[str]], instructions: Tuple[int, int, int]) -> str:
    for instruction in instructions:
        move, from_stack, to_stack = parse_instruction(instruction)
        from_stack -= 1
        to_stack -= 1
        for _ in range(move):
            stacks[to_stack].append(stacks[from_stack].pop())

    answer = [stack[-1] for stack in stacks]
    return ''.join(answer)

def part_2(input):
    pass


def create_stack(stacks_input: str) -> List[List[str]]:
    *crates, num_of_stacks = stacks_input.split('\n')

    stacks = [[] for _ in range(len(num_of_stacks.split()))]

    crates.reverse()
    for crate in crates:
        for stackId, i in enumerate(range(1, len(crates[0]), 4)):
            if crate[i].strip():
                stacks[stackId].append(crate[i])

    return stacks


if __name__ == '__main__':
    file_path = './5-Supply_Stacks/input.txt'
    stacks_input, instructions = process_inputs(file_path)

    stacks = create_stack(stacks_input)

    print("--Part 1--")
    print(part_1(stacks, instructions.split('\n')))

    print("--Part 2--")
    print(part_2(input))
