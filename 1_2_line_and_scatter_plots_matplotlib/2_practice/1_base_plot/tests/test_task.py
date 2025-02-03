from typing import ClassVar

import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)

    def test_01_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_01_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_01_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=1)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=1)

    def test_02_1_line_position(self):
        self.checkLinePosition(self.fig.axes[0], expected_x=self.data["x"], expected_y=self.data["approximated_y"])

    def test_02_2_line_color(self):
        self.checkLineColor(self.fig.axes[0], expected_color="navy")

    def test_02_3_line_transparency(self):
        self.checkLineTransparency(self.fig.axes[0], expected_alpha=1)

    def test_03_1_scatter_position(self):
        self.checkCollectionPosition(self.fig.axes[0], expected_x=self.data["x"], expected_y=self.data["y"])

    def test_03_2_scatter_color(self):
        self.checkCollectionColor(self.fig.axes[0], expected_facecolor="grey")

    def test_03_3_scatter_transparency(self):
        self.checkCollectionTransparency(self.fig.axes[0], expected_alpha=0.05)

    def test_04_spines(self):
        self.checkSpineVisibility(self.fig.axes[0], position="top", expected_visibility=False)
        self.checkSpineVisibility(self.fig.axes[0], position="bottom", expected_visibility=True)
        self.checkSpineVisibility(self.fig.axes[0], position="left", expected_visibility=True)
        self.checkSpineVisibility(self.fig.axes[0], position="right", expected_visibility=False)

    def test_05_1_x_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=[-4, 0, 4], axis="x")

    def test_05_2_x_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="x", axis="x")

    def test_06_1_y_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=[-1.5, 0, 1.5], axis="y")

    def test_06_2_y_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="y", axis="y")
