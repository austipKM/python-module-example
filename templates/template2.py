import pandas as pd
from .base_template import BaseTemplate


class Template2(BaseTemplate):
    def __init__(self):
        self.df = pd.DataFrame({
            "x": [1, 2, 3],
            "y": [4, 5, 6],
            "z": [0, 1, 2]
        })

    def aggregate(self):
        pass

    def create_bar_plot(self):
        pass

    def create_histogram(self):
        pass
