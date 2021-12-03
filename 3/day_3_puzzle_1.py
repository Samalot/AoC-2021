import Reader


def run():
    size = 12
    counts = [0 for i in range(size)]

    for data in Reader.read("input"):
        for i in range(len(data)):
            if data[i] == "0":
                counts[i] -= 1
            else:
                counts[i] += 1

    gamma = sum([[0 if n < 0 else 1 for n in counts][i] * 2 ** (size - 1 - i) for i in range(size)])
    epsilon = sum([[1 if n < 0 else 0 for n in counts][i] * 2 ** (size - 1 - i) for i in range(size)])

    return gamma * epsilon


print(f'Answer: {run()}')
