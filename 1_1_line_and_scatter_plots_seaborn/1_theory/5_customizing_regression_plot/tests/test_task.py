from typing import ClassVar

import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

    def test_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.lmplot")

    def test_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, 1)

    def test_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, 2)
        self.checkNumberOfLines(self.fig.ax, 1)

    def test_4_data_position(self):
        expected_fig = sns.lmplot(self.data, x="user_score", y="critic_score")
        expected_line_x, expected_line_y = expected_fig.ax.lines[0].get_xydata().T

        self.checkLinePosition(self.fig.ax, expected_line_x, expected_line_y)
        self.checkCollectionPosition(self.fig.ax, self.data["user_score"], self.data["critic_score"])

    def test_5_transparency(self):
        self.checkLineTransparency(self.fig.ax, 1)
        self.checkCollectionTransparency(self.fig.ax, 0.1)

    def test_6_color(self):
        self.checkLineColor(self.fig.ax, "firebrick")
        self.checkCollectionColor(self.fig.ax, "C0")
