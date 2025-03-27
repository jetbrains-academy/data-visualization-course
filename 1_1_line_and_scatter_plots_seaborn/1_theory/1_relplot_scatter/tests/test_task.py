from typing import ClassVar

import pandas as pd
import seaborn as sns

from test_framework import CollectionTestMixin

from data import preprocess, read
from task import plot


class PlotTestCase(CollectionTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.relplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=1)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)

    def test_2_1_scatter_position(self):
        self.checkCollectionPosition(
            self.fig.ax,
            expected_x=self.data["user_score"],
            expected_y=self.data["critic_score"],
        )
