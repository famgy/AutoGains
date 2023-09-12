import numpy as np


class GameFrame:
    def __init__(self, frame_data, timestamp=None):
        self.frame_array = frame_data
        self.timestamp = timestamp
