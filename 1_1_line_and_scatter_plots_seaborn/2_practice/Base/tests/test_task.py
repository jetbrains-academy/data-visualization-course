from typing import ClassVar

import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, 1)

    def test_1_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, 2)
        self.checkNumberOfLines(self.fig.ax, 1)

    def test_2_1_line_position(self):
        expected_fig = sns.lmplot(self.data, x="x", y="y")
        expected_line_x, expected_line_y = expected_fig.ax.lines[0].get_xydata().T
        self.checkLinePosition(self.fig.ax, expected_line_x, expected_line_y)

    def test_2_2_line_color(self):
        self.checkLineColor(self.fig.ax, "navy")

    def test_2_3_line_transparency(self):
        self.checkLineTransparency(self.fig.ax, 1)

    def test_3_1_scatter_positions(self):
        self.checkCollectionPosition(self.fig.ax, self.data["x"], self.data["y"])

    def test_3_2_scatter_color(self):
        self.checkCollectionColor(self.fig.ax, "grey")

    def test_3_3_scatter_transparency(self):
        self.checkCollectionTransparency(self.fig.ax, 0.05)
