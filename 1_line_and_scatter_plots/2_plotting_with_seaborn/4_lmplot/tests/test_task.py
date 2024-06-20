from typing import ClassVar

import pandas as pd
import seaborn as sns

from common.seaborn_test_mixins import BaseTestMixin
from data import preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

    def test_1_return_type(self):
        self.checkReturnType(self.fig)

    def test_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig, 1)

    def test_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig, 2)
        self.checkNumberOfLines(self.fig, 1)
