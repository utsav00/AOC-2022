"""
X: Rock defeats Scissors
Y: Paper defeats Rock
Z: Scissors defeats Paper
"""

def process_inputs(file_path):
    with open(file_path, 'r') as f:
        content = f.read().split('\n')
        return [turn.split(' ') for turn in content]

map = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points = {'X': 1, 'Y': 2, 'Z': 3}
win = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
loss = dict((v,k) for k, v in win.items())

def get_score(opponent, player):
    result = 0
    result += points[player]
    if opponent == player:
        result += 3
    elif win[player] == opponent:
        result += 6
    return result

def part_1(input):
    result = 0
    for turn in input:
        opponent, player = turn
        opponent = map[opponent]
        result += get_score(opponent, player)
    return result

def part_2(input):
    result = 0

if __name__ == '__main__':
    file_path = './2-Rock_Paper_Scissors/input.txt'
    input = process_inputs(file_path)
    print(part_1(input))