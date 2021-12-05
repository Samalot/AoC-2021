import Reader


def run():
    maxX, maxY = 0, 0
    points = []
    for data in Reader.read("input"):
        pointA, pointB = data.split(" -> ")
        x1, y1 = pointA.split(",")
        x2, y2 = pointB.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if max(x1, x2) > maxX:
            maxX = max(x1, x2)
        if max(y1, y2) > maxY:
            maxY = max(y1, y2)

        if x1 == x2:
            points.append([0, (x1, min(y1, y2)), (x2, max(y1, y2))])
        elif y1 == y2:
            points.append([1, (min(x1, x2), y1), (max(x1, x2), y2)])
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            points.append([2 if y1 > y2 else 3, (x1, y1), (x2, y2)])

    grid = [[0 for x in range(maxX + 1)] for y in range(maxY + 1)]
    for point in points:
        if point[0] == 0:
            for y in range(point[1][1], point[2][1] + 1):
                grid[y][point[1][0]] += 1
        else:
            for x in range(point[1][0], point[2][0] + 1):
                if point[0] == 1:
                    grid[point[1][1]][x] += 1
                elif point[0] == 2:
                    offset = x - point[1][0]
                    grid[point[1][1] - offset][x] += 1
                else:
                    offset = x - point[1][0]
                    grid[point[1][1] + offset][x] += 1

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 1:
                total += 1

    return total


print(f'Answer: {run()}')
