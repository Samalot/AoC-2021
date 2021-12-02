import Reader


def run():
    previous = -100000
    window = [-10000, -10000, -10000]

    total = -3
    for data in Reader.read("input"):
        window[0] = window[1]
        window[1] = window[2]
        window[2] = int(data)
        num = sum(window)

        if num > previous:
            total += 1

        previous = num

    return total


print(f'Answer: {run()}')

