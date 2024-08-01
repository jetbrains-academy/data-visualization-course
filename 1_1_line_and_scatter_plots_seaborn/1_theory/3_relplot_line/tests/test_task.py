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
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.relplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, 1)

    def test_1_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, 1)
        self.checkNumberOfLines(self.fig.ax, 1)

    def test_2_1_line_position(self):
        position = self.data.groupby("user_score")["critic_score"].mean()
        self.checkLinePosition(self.fig.ax, position.index, position)

    def test_2_2_line_transparency(self):
        self.checkLineTransparency(self.fig.ax, 1)

    def test_2_3_line_color(self):
        self.checkLineColor(self.fig.ax, "C0")
