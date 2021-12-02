import Reader


def run():
    numbers = []
    for data in Reader.read("input"):
        numbers.append(int(data))

    return 0


print(f'Answer: {run()}')
