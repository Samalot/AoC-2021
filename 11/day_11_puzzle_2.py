import Reader


class Grid:
    def __init__(self):
        self.grid = []
        self.total_octopuses = 0

    def add_row(self, data):
        new_row = [int(c) for c in data]
        self.grid.append(new_row)
        self.total_octopuses += len(new_row)

    def increase_energy(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.grid[y][x] += 1

    def find_triggered(self):
        triggered = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] > 9:
                    triggered.append((x, y))
        return triggered

    def flash(self):
        flashed_this_turn = set()
        to_flash = self.find_triggered()

        while len(to_flash) > 0:
            next_to_flash = []
            for octopus in to_flash:
                if not flashed_this_turn.__contains__(octopus):
                    pos_x, pos_y = octopus[0], octopus[1]
                    flashed_this_turn.add(octopus)

                    neighbors = [
                        (x, y)
                        for x in range(max(0, pos_x - 1), min(len(self.grid[0]), pos_x + 2))
                        for y in range(max(0, pos_y - 1), min(len(self.grid), pos_y + 2))
                    ]
                    for neighbor_octopus in neighbors:
                        self.grid[neighbor_octopus[1]][neighbor_octopus[0]] += 1
                        if self.grid[neighbor_octopus[1]][neighbor_octopus[0]] > 9:
                            next_to_flash.append(neighbor_octopus)

            to_flash = next_to_flash

        for octopus in flashed_this_turn:
            self.grid[octopus[1]][octopus[0]] = 0

        return len(flashed_this_turn)


def run():
    grid = Grid()
    for data in Reader.read("input"):
        grid.add_row(data)

    step = 1
    while True:
        grid.increase_energy()
        if grid.flash() == grid.total_octopuses:
            return step
        step += 1


print(f'Answer: {run()}')
