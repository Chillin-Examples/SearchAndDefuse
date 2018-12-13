# -*- coding: utf-8 -*-


class FogDetector:

    def __init__(self, terrorist_vision_distance, police_vision_distance):
        self.police_vision_distance = police_vision_distance
        self.terrorist_vision_distance = terrorist_vision_distance

    def compute_agent_fog(self, agent):
        pass

    def compute_polices_fogs(self, positions):
        pass

    def compute_terrorists_fogs(self, positions):
        pass
