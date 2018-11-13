class GuiHandler:
    world = None
    sides = []
    canvas = None
    def __init__(self, world, sides, canvas):
        self.world = world
        self.sides = sides
        self.canvas = canvas

    def update(self, gui_events):
        pass

    def initialize(self):
        pass