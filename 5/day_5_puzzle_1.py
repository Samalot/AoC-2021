import Reader


def run():
    maxX, maxY = 0, 0
    points = []
    for data in Reader.read("input"):
        pointA, pointB = data.split(" -> ")
        x1, y1 = pointA.split(",")
        x2, y2 = pointB.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2 or y1 == y2:
            if max(x1, x2) > maxX:
                maxX = max(x1, x2)
            if max(y1, y2) > maxY:
                maxY = max(y1, y2)

            if x1 == x2:
                points.append([False, x1, min(y1, y2), max(y1, y2)])
            else:
                points.append([True, y1, min(x1, x2), max(x1, x2)])

    grid = [[0 for x in range(maxX + 1)] for y in range(maxY + 1)]
    for point in points:
        for i in range(point[2], point[3] + 1):
            if point[0]:
                grid[point[1]][i] += 1
            else:
                grid[i][point[1]] += 1

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 1:
                total += 1

    return total



print(f'Answer: {run()}')
