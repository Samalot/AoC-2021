import Reader


def run():
    positions = []
    for data in Reader.read("input"):
        positions = sorted(list(map(lambda x: int(x), data.split(","))))

    median = positions[len(positions) // 2]
    fuel_used = list(map(lambda x: abs(x - median), positions))

    return sum(fuel_used)


print(f'Answer: {run()}')
