from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    aggregated_data: ClassVar[pd.DataFrame]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.aggregated_data = aggregate(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], 1)
        self.checkContainerType(self.fig.axes[0], BarContainer)
        self.checkNumberOfBars(self.fig.axes[0], self.data["platform"].nunique())

    def test_2_1_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="horizontal")

    def test_2_2_bar_values(self):
        self.checkBarValues(self.fig.axes[0], self.aggregated_data["count"].to_list())

    def test_2_3_bar_labels(self):
        self.checkTickLabels(self.fig.axes[0], self.aggregated_data["platform"].to_list(), axis="y")
