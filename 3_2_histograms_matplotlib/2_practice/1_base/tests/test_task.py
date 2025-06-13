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
    cities: ClassVar[list[str]]
    bins: ClassVar[list]
    color_map: ClassVar[dict[str, str]]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)

        cls.cities = ["Yerevan", "Belgrade"]
        cls.bins = get_bins(data)

        cls.color_map = {
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
                expected_bins=self.bins,
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
                expected_alpha=1,
                container_number=patch_number,
                histtype="step",
            )

    def test_2_4_bar_colors(self):
        for patch_number, city in enumerate(self.cities):
            self.checkBarColor(
                self.fig.axes[0],
                expected_facecolors=self.color_map[city],
                container_number=patch_number,
                histtype="step",
            )

    def test_3_labels(self):
        self.checkLabel(self.fig.axes[0], expected_label="Sales", axis="x")
        self.checkLabel(self.fig.axes[0], expected_label="Probability", axis="y")

    def test_4_title(self):
        self.checkTitle(self.fig.axes[0], expected_title="Sales Distribution in Belgrade and Yerevan")

    def test_5_1_legend(self):
        self.checkLegendExists(self.fig.axes[0])
        self.checkLegendLabels(self.fig.axes[0], expected_labels=self.cities)

    def test_5_2_legend_colors(self):
        self.checkLegendHandleColors(self.fig.axes[0], expected_handle_colors=list(self.color_map.values()))
