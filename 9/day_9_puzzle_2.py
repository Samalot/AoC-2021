import Reader


def validate_coord(x, y, data):
    return not (data[y][x] == "*" or data[y][x] == '9')


def run():
    map = []
    for data in Reader.read("input"):
        map.append([c for c in data])

    basins = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if validate_coord(x, y, map):
                current_basin = 0
                queue = [(y, x)]
                while len(queue) > 0:
                    coord = queue.pop()
                    coord_y, coord_x = coord[0], coord[1]
                    if validate_coord(coord_x, coord_y, map):
                        if coord_y > 0 and validate_coord(coord_x, coord_y - 1, map):
                            queue.append((coord_y - 1, coord_x))

                        if coord_y < len(map) - 1 and validate_coord(coord_x, coord_y + 1, map):
                            queue.append((coord_y + 1, coord_x))

                        if coord_x > 0 and validate_coord(coord_x - 1, coord_y, map):
                            queue.append((coord_y, coord_x - 1))

                        if coord_x < len(map[0]) - 1 and validate_coord(coord_x + 1, coord_y, map):
                            queue.append((coord_y, coord_x + 1))

                        current_basin += 1
                        map[coord_y][coord_x] = '*'

                basins.append(current_basin)

    sorted_basins = sorted(basins, reverse=True)
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]


print(f'Answer: {run()}')