class GuiEvent:
    type = None
    extra_properties = {}

    def __init__(self, type):
        self.type = type
#GuiEventType