import pandas as pd
from .base_template import BaseTemplate


class Template1(BaseTemplate):
    def __init__(self):
        self.df = pd.DataFrame({
            "x": ['Day 1', 'Day 2', 'Day 3'],
            "y": [10, 20, 30],
            "z": [True, False, True]
        })

    def aggregate(self):
        pass

    def create_bar_plot(self):
        pass

    def create_histogram(self):
        pass
