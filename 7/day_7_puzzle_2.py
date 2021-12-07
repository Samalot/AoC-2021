import Reader


def run():
    positions = []
    for data in Reader.read("input"):
        positions = list(map(lambda x: int(x), data.split(",")))

    mean = sum(positions) // len(positions)
    distance_moved = list(map(lambda x: abs(x - mean), positions))
    fuel_used = list(map(lambda x: x * (x + 1)/2, distance_moved))

    return int(sum(fuel_used))


print(f'Answer: {run()}')
