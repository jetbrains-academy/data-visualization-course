from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import AxisTestMixin, HistTestMixin

from data import filter_by_publisher_and_global_sales, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    bins: ClassVar[int]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)
        cls.publishers = ["Electronic Arts", "Ubisoft"]
        cls.bins = 10

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_hist_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], expected_number=2)
        for container_number, publisher in enumerate(self.publishers):
            filtered_data = filter_by_publisher_and_global_sales(self.data, publisher)
            bins = np.histogram_bin_edges(filtered_data["global_sales"], bins=self.bins)
            self.checkContainerType(self.fig.axes[0], expected_type=BarContainer, container_number=container_number)
            self.checkBarBins(self.fig.axes[0], expected_bins=bins.tolist(), container_number=container_number)

    def test_2_1_bar_height(self):
        for container_number, publisher in enumerate(self.publishers):
            filtered_data = filter_by_publisher_and_global_sales(self.data, publisher)
            weights = np.ones_like(filtered_data["global_sales"]) / filtered_data["global_sales"].shape[0]
            counts, _ = np.histogram(filtered_data["global_sales"], bins=self.bins, weights=weights)
            self.checkBarHeights(self.fig.axes[0], expected_values=counts.tolist(), container_number=container_number)

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="vertical")

    def test_2_3_bar_transparency(self):
        for container_number, _ in enumerate(self.publishers):
            self.checkBarTransparency(self.fig.axes[0], expected_alpha=0.7, container_number=container_number)
