from typing import ClassVar

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import AxisTestMixin, HistTestMixin, LegendTestMixin, TitleTestMixin

from data import get_bins, get_city_sales, get_weights, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin, LegendTestMixin, TitleTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)
        cls.cities = ["Yerevan", "Belgrade"]
        cls.bins = get_bins(data)
        cls.color_map = {
            "Yerevan": "pink",
            "Belgrade": "grey",
        }
        cls.edge_color_map = {
            "Yerevan": "crimson",
            "Belgrade": "black",
        }

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_hist_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        self.checkNumberOfContainers(self.fig.axes[0], expected_number=0)
        self.checkNumberOfPatches(self.fig.axes[0], expected_number=2)
        for patch_number in range(len(self.cities)):
            self.checkPatchType(self.fig.axes[0], expected_type=Polygon, patch_number=patch_number)

    def test_2_1_bar_bins(self):
        for patch_number in range(len(self.cities)):
            self.checkBarBins(
                self.fig.axes[0],
                expected_bins=self.bins.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_2_2_bar_height(self):
        for patch_number, city in enumerate(self.cities):
            city_sales = get_city_sales(self.data, city)
            weights = get_weights(city_sales)
            counts, _ = np.histogram(city_sales, bins=self.bins, weights=weights)
            self.checkBarHeights(
                self.fig.axes[0],
                expected_values=counts.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_2_3_bar_transparency(self):
        for patch_number in range(len(self.cities)):
            self.checkBarTransparency(
                self.fig.axes[0],
                expected_alpha=0.5,
                container_number=patch_number,
                histtype="step",
            )

    def test_2_4_bar_legend(self):
        self.checkLegendExists(self.fig.axes[0])
        self.checkLegendLabels(self.fig.axes[0], expected_labels=self.cities)

    def test_3_1_bar_colors(self):
        for patch_number, city in enumerate(self.cities):
            self.checkStepHistColor(
                self.fig.axes[0],
                expected_facecolor=self.color_map[city],
                container_number=patch_number,
            )

    def test_3_2_bar_edge_colors(self):
        for patch_number, city in enumerate(self.cities):
            self.checkStepHistEdgeColor(
                self.fig.axes[0],
                expected_edgecolor=self.edge_color_map[city],
                container_number=patch_number,
            )

    def test_4_labels(self):
        self.checkLabel(self.fig.axes[0], expected_label="Sales", axis="x")
        self.checkLabel(self.fig.axes[0], expected_label="Probability", axis="y")
