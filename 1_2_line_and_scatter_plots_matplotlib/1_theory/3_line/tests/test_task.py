from typing import ClassVar

import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=1)

    def test_2_1_line_position(self):
        self.checkLinePosition(
            self.fig.axes[0],
            expected_x=self.data["user_score"],
            expected_y=self.data["critic_score"],
        )

    def test_2_2_line_transparency(self):
        self.checkLineTransparency(self.fig.axes[0], expected_alpha=1)

    def test_2_3_line_color(self):
        self.checkLineColor(self.fig.axes[0], "C0")
