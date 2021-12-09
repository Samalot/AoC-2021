import Reader


def run():
    map = []
    for data in Reader.read("input"):
        map.append(data)

    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            val = map[y][x]
            if all([
                map[y - 1][x] > val if y > 0 else True,
                map[y + 1][x] > val if y < len(map) - 1 else True,
                map[y][x - 1] > val if x > 0 else True,
                map[y][x + 1] > val if x < len(map[0]) - 1  else True
            ]):
                total += (1 + int(val))

    return total


print(f'Answer: {run()}')
