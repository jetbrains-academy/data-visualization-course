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

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.lmplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=2)
        self.checkNumberOfLines(self.fig.ax, expected_number=1)

    def test_2_1_line_position(self):
        expected_fig = sns.lmplot(self.data, x="user_score", y="critic_score")
        expected_line_x, expected_line_y = expected_fig.ax.lines[0].get_xydata().T
        self.checkLinePosition(self.fig.ax, expected_x=expected_line_x, expected_y=expected_line_y)

    def test_2_2_line_color(self):
        self.checkLineColor(self.fig.ax, expected_color="firebrick")

    def test_2_3_line_transparency(self):
        self.checkLineTransparency(self.fig.ax, expected_alpha=1)

    def test_3_1_scatter_position(self):
        self.checkCollectionPosition(
            self.fig.ax,
            expected_x=self.data["user_score"],
            expected_y=self.data["critic_score"],
        )

    def test_3_2_transparency(self):
        self.checkCollectionTransparency(self.fig.ax, expected_alpha=0.1)

    def test_3_3_color(self):
        self.checkCollectionColor(self.fig.ax, expected_facecolor=None)
