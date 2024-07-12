from typing import ClassVar

import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import preprocess, read, aggregate
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

    def test_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 1)
        self.checkNumberOfLines(self.fig.axes[0], 1)

    def test_4_data_position(self):
        aggregated_data = aggregate(self.data)
        self.checkLinePosition(self.fig.axes[0], aggregated_data["user_score"], aggregated_data["critic_score"])
        self.checkCollectionPosition(self.fig.axes[0], self.data["user_score"], self.data["critic_score"])
