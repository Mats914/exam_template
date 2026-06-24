class Item:
    """Representerar saker man kan plocka upp."""

    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [
    Item("carrot", 20),
    Item("apple", 20),
    Item("strawberry", 20),
    Item("cherry", 20),
    Item("watermelon", 20),
    Item("radish", 20),
    Item("cucumber", 20),
    Item("meatball", 20)
]


def randomize(grid):
    for item in pickups:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()

            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break