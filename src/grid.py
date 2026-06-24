import random


class Grid:
    """Representerar spelplanen."""

    width = 36
    height = 12

    empty = "."
    wall = "■"

    def __init__(self):
        self.data = [
            [self.empty for x in range(self.width)]
            for y in range(self.height)
        ]

    def get(self, x, y):
        return self.data[y][x]

    def set(self, x, y, value):
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        self.set(x, y, self.empty)

    def __str__(self):

        xs = ""

        for y in range(len(self.data)):
            row = self.data[y]

            for x in range(len(row)):

                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])

            xs += "\n"

        return xs

    def make_walls(self):

        # Yttre väggar

        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # Inre väggar

        for x in range(5, 15):
            self.set(x, 4, self.wall)

        for y in range(6, 10):
            self.set(20, y, self.wall)

        for x in range(22, 30):
            self.set(x, 8, self.wall)

    def get_random_x(self):
        return random.randint(0, self.width - 1)

    def get_random_y(self):
        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):
        return self.get(x, y) == self.empty