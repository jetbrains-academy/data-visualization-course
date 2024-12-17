from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, filter_platforms, preprocess, read
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

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure, expected_function="plt.bar")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], 1)
        self.checkContainerType(self.fig.axes[0], BarContainer)
        self.checkNumberOfBars(self.fig.axes[0], filter_platforms(self.data)["platform"].nunique())

    def test_2_1_bar_position(self):
        self.checkBarsPosition(self.fig.axes[0], aggregate(filter_platforms(self.data))["count"].to_list())

    def test_2_2_bar_layout(self):
        self.checkBarsLayout(self.fig.axes[0], expected_layout="horizontal")

    def test_2_3_bar_labels(self):
        self.checkTickLabels(self.fig.axes[0], aggregate(filter_platforms(self.data))["platform"].to_list(), axis="y")

    def test_2_4_bar_colors(self):
        self.checkBarsColor(self.fig.axes[0], expected_facecolors=["gray", "blue", "green", "cyan"])

    def test_3_labels(self):
        self.checkLabel(self.fig.axes[0], "Count", "x")
        self.checkLabel(self.fig.axes[0], "Platform", "y")

    def test_5_title(self):
        self.checkTitle(self.fig.axes[0], "Number of games per platform")
