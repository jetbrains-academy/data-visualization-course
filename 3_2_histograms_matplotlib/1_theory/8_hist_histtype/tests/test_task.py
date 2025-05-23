from typing import ClassVar

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import AxisTestMixin, HistTestMixin, LegendTestMixin, TitleTestMixin

from data import filter_by_publisher, filter_by_global_sales, get_bins, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin, LegendTestMixin, TitleTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    publishers: ClassVar[list[str]]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.publishers = ["Electronic Arts", "Ubisoft"]
        cls.bins = get_bins(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_hist_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        self.checkNumberOfContainers(self.fig.axes[0], expected_number=0)
        self.checkNumberOfPatches(self.fig.axes[0], expected_number=2)
        for patch_number in range(len(self.publishers)):
            self.checkPatchType(self.fig.axes[0], expected_type=Polygon, patch_number=patch_number)

    def test_2_1_bar_bins(self):
        for patch_number in range(len(self.publishers)):
            self.checkBarBins(
                self.fig.axes[0],
                expected_bins=self.bins.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_2_2_bar_height(self):
        for patch_number, publisher in enumerate(self.publishers):
            filtered_data = filter_by_publisher(self.data, publisher)
            filtered_data = filter_by_global_sales(filtered_data)
            weights = np.ones_like(filtered_data["global_sales"]) / filtered_data["global_sales"].shape[0]
            counts, _ = np.histogram(filtered_data["global_sales"], bins=self.bins, weights=weights)
            self.checkBarHeights(
                self.fig.axes[0],
                expected_values=counts.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_2_3_bar_transparency(self):
        for patch_number in range(len(self.publishers)):
            self.checkBarTransparency(
                self.fig.axes[0],
                expected_alpha=0.7,
                container_number=patch_number,
                histtype="step",
            )

    def test_3_labels(self):
        self.checkLabel(self.fig.axes[0], expected_label="Global Sales (millions)", axis="x")
        self.checkLabel(self.fig.axes[0], expected_label="Proportion", axis="y")

    def test_4_title(self):
        self.checkTitle(self.fig.axes[0], expected_title="Global Sales Distribution for Electronic Arts and Ubisoft")

    def test_5_bar_legend(self):
        self.checkLegendExists(self.fig.axes[0])
        self.checkLegendLabels(self.fig.axes[0], expected_labels=self.publishers)
