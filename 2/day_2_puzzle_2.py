import Reader


def run():
    depth, horizontal, aim = 0, 0, 0

    for data in Reader.read("input"):
        direction, amount = data.split(" ")

        if direction == "up":
            aim -= int(amount)

        elif direction == "down":
            aim += int(amount)

        else:
            horizontal += int(amount)
            depth += aim * int(amount)

    return depth * horizontal


print(f'Answer: {run()}')