from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, get_number_of_decades, preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    aggregated_data: ClassVar[pd.DataFrame]
    number_of_decades: ClassVar[int]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.aggregated_data = aggregate(cls.data)
        cls.number_of_decades = get_number_of_decades(cls.aggregated_data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], 1)
        self.checkContainerType(self.fig.axes[0], BarContainer)
        self.checkNumberOfBars(self.fig.axes[0], self.aggregated_data["decade"].nunique())

    def test_2_1_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="vertical")

    def test_2_2_bar_values(self):
        expected_values = self.aggregated_data[self.aggregated_data["region"] == "na"]["sales"].to_list()
        self.checkBarValues(self.fig.axes[0], expected_values)

    def test_2_3_bar_width(self):
        self.checkBarWidth(self.fig.axes[0], 0.8)

    def test_2_4_bar_positions(self):
        self.checkBarPositions(self.fig.axes[0], list(range(self.number_of_decades)), axis="x")

    def test_3_title(self):
        self.checkTitle(self.fig.axes[0], None)
