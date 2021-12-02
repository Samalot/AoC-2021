import Reader


def run():
    previous = -1000

    total = -1
    for data in Reader.read("input"):
        num = int(data)
        if num > previous:
            total += 1
        previous = num

    return total


print(f'Answer: {run()}')
