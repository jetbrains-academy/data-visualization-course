from typing import ClassVar

from matplotlib.container import BarContainer
import numpy as np
import pandas as pd
import seaborn as sns

from test_framework import AxisTestMixin, HistTestMixin

from data import filter_by_global_sales, filter_by_publisher, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.fig = plot(data)
        cls.data = filter_by_publisher(data)
        cls.data = filter_by_global_sales(cls.data)

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
        for container_number in range(len(self.publishers)):
            self.checkContainerType(self.fig.ax, expected_type=BarContainer, container_number=container_number)

    def test_2_1_bar_bins(self):
        for container_number in range(len(self.publishers)):
            self.checkBarBins(self.fig.ax, expected_bins=self.bins.tolist(), container_number=container_number)

    def test_2_2_bar_height(self):
        for container_number, publisher in enumerate(self.publishers):
            filtered_dataset = self.data[self.data["publisher"] == publisher]
            weights = np.ones_like(filtered_dataset["global_sales"]) / filtered_dataset.shape[0]
            counts, _ = np.histogram(filtered_dataset["global_sales"], bins=self.bins, weights=weights)
            self.checkBarHeights(self.fig.ax, expected_values=counts.tolist(), container_number=container_number)

    def test_2_3_bar_layout(self):
        self.checkBarLayout(self.fig.ax, expected_layout="vertical")
