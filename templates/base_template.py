"""All other templates should inherit from this base template.

    classes:
        BaseTemplate: the baseline template that all templates should be based off of. If you have a method you want to use across all templates, you can define that here (see execute() method)
"""

from abc import ABC, abstractmethod
import pandas as pd


class BaseTemplate(ABC):
    @abstractmethod
    def aggregate(self):
        """The implementation of this has intentionally not been defined. 
        Think of this as a placeholder for other templates to implement the specifics
        """
        pass

    def get_df(self) -> pd.DataFrame:
        """Returns the template's current dataframe or a new dataframe

        Returns:
            pd.DataFrame: Current instance's dataframe
        """
        if not isinstance(self.df, pd.DataFrame):
            return pd.DataFrame()

        return self.df
