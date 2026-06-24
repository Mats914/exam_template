class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        next_x = self.pos_x + dx
        next_y = self.pos_y + dy

        return grid.get(next_x, next_y) != grid.wall