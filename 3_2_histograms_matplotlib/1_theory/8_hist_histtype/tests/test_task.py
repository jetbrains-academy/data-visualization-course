from typing import ClassVar

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import AxisTestMixin, HistTestMixin

from data import filter_by_publisher_and_global_sales, get_max_sales, get_min_sales, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)
        cls.publishers = ["Electronic Arts", "Ubisoft"]
        min, max = get_min_sales(data), get_max_sales(data)
        cls.bins = np.linspace(min, max, num=11)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_hist_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        self.checkNumberOfContainers(self.fig.axes[0], expected_number=0)
        self.checkNumberOfPatches(self.fig.axes[0], expected_number=2)
        for patch_number, _ in enumerate(self.publishers):
            self.checkPatchType(self.fig.axes[0], expected_type=Polygon, patch_number=patch_number)
            self.checkStepHistBins(self.fig.axes[0], expected_bins=self.bins.tolist(), patch_number=patch_number)

    def test_2_1_bar_height(self):
        for patch_number, publisher in enumerate(self.publishers):
            filtered_data = filter_by_publisher_and_global_sales(self.data, publisher)
            weights = np.ones_like(filtered_data["global_sales"]) / filtered_data["global_sales"].shape[0]
            counts, _ = np.histogram(filtered_data["global_sales"], bins=self.bins, weights=weights)
            self.checkStepHistHeights(self.fig.axes[0], expected_values=counts.tolist(), patch_number=patch_number)

    def test_2_2_bar_transparency(self):
        for patch_number, _ in enumerate(self.publishers):
            self.checkStepHistTransparency(self.fig.axes[0], expected_alpha=0.7, patch_number=patch_number)
