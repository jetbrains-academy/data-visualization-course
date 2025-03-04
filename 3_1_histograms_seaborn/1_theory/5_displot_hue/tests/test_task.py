from typing import ClassVar

from matplotlib.container import BarContainer
import numpy as np
import pandas as pd
import seaborn as sns

from test_framework import AxisTestMixin, HistTestMixin, LegendTestMixin

from data import filter_by_publisher_and_global_sales, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin, LegendTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.fig = plot(data)
        cls.data = filter_by_publisher_and_global_sales(data)
        cls.bins = np.histogram_bin_edges(cls.data["global_sales"], bins=10)
        cls.publishers = cls.data["publisher"].unique()[::-1]

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.displot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_displot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=0)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)

        # Bars
        self.checkNumberOfContainers(self.fig.ax, expected_number=2)
        for container_number, _ in enumerate(self.publishers):
            self.checkContainerType(self.fig.ax, expected_type=BarContainer, container_number=container_number)
            self.checkBarBins(self.fig.ax, expected_bins=self.bins.tolist(), container_number=container_number)

    def test_2_1_bar_height(self):
        for container_number, publisher in enumerate(self.publishers):
            counts, _ = np.histogram(self.data[self.data["publisher"] == publisher]["global_sales"], bins=self.bins)
            self.checkBarHeights(self.fig.ax, expected_values=counts.tolist(), container_number=container_number)

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.ax, expected_layout="vertical")
