def process_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().split('\n\n')
        return [sum(list(map(int, each_total.split('\n')))) for each_total in content]


def first_part(calories):
    return max(calories)


def second_part(calories):
    return sum(sorted(calories, reverse=True)[0:3])


if __name__ == "__main__":
    file_path = './1-Calorie_Counting/calories.txt'
    calories = process_input(file_path)

    print("--Part 1--")
    print(first_part(calories))

    print("--Part 2--")
    print(second_part(calories))
