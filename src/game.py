from src.grid import Grid
from src.player import Player
from src import pickups


class GameState:

    def __init__(self):

        # nära mitten av kartan
        self.player = Player(18, 6)

        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)

        self.g.make_walls()

        pickups.randomize(self.g)


def print_status(game_grid, state):

    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)


def move_player(state, dx, dy):

    if not state.player.can_move(dx, dy, state.g):
        print("Wall!")
        return

    state.player.move(dx, dy)

    # Floor is lava
    state.score -= 1

    maybe_item = state.g.get(
        state.player.pos_x,
        state.player.pos_y
    )

    if isinstance(maybe_item, pickups.Item):

        state.score += maybe_item.value

        state.inventory.append(maybe_item.name)

        print(
            f"You found a {maybe_item.name}, "
            f"+{maybe_item.value} points."
        )

        state.g.clear(
            state.player.pos_x,
            state.player.pos_y
        )


def show_inventory(state):

    print("\nInventory")

    if len(state.inventory) == 0:
        print("Empty")
        return

    for item in state.inventory:
        print("-", item)


def start(state):

    command = ""

    while command not in ["q", "x"]:

        print_status(state.g, state)

        command = input(
            "Use WASD to move, I inventory, Q/X quit: "
        )

        command = command.casefold()[:1]

        if command == "w":
            move_player(state, 0, -1)

        elif command == "s":
            move_player(state, 0, 1)

        elif command == "a":
            move_player(state, -1, 0)

        elif command == "d":
            move_player(state, 1, 0)

        elif command == "i":
            show_inventory(state)

    print("Thank you for playing!")


if __name__ == "__main__":
    game_state = GameState()
    start(game_state)