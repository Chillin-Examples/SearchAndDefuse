class LogicHandler:
    world = None
    sides = []
    def __init__(self, world, sides):
        self.world = world
        self.sides = sides

    def store_command(self, side_name, command):
        pass

    def clear_commands(self):
        pass

    def process(self, current_cycle):
        pass

    def get_client_world(self, side_name):
        pass

    def check_end_game(self):
        pass