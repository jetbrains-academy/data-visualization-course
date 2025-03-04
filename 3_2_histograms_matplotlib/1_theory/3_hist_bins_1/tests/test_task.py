from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import AxisTestMixin, HistTestMixin

from data import get_logarithmic_bins, preprocess, read
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    counts: ClassVar[np.ndarray]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.bins = get_logarithmic_bins(data, 100)
        cls.counts, _ = np.histogram(data["global_sales"], bins=cls.bins)
        cls.fig = plot(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], expected_number=1)
        self.checkContainerType(self.fig.axes[0], expected_type=BarContainer)
        self.checkBarBins(self.fig.axes[0], expected_bins=self.bins.tolist())

    def test_1_4_x_scale(self):
        self.checkAxisScale(self.fig.axes[0], expected_scale="log", axis="x")

    def test_2_1_bar_height(self):
        self.checkBarHeights(self.fig.axes[0], expected_values=self.counts.tolist())

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="vertical")
