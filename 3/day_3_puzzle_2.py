import Reader


def reduce(data, flipped):
    array = data
    bit = 0
    while len(array) > 1 and bit < len(array[0]):
        ones = list(filter(lambda x: (x[bit] == "1"), array))
        zeros = list(filter(lambda x: (x[bit] == "0"), array))
        array = (zeros if not flipped else ones) if len(ones) >= len(zeros) else (ones if not flipped else zeros)
        bit += 1
    return int(array[0], 2)


def run():
    rawData = []
    for data in Reader.read("input"):
        rawData.append(data)

    oxygen = reduce(rawData, False)
    scrubber = reduce(rawData, True)
    return oxygen * scrubber


print(f'Answer: {run()}')

