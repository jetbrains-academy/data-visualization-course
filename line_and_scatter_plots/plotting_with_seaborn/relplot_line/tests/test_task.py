from typing import ClassVar

import pandas as pd
import seaborn as sns

from common.seaborn_test_mixins import BaseTestMixin
from data import read, preprocess
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
        self.checkReturnType(self.fig)

    def test_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig, 1)

    def test_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig, 1)
        self.checkNumberOfLines(self.fig, 1)

    def test_5_data_position(self):
        position = self.data.groupby('user_score')['critic_score'].mean()
        self.checkLinePosition(self.fig, position.index, position)

    def test_6_transparency(self):
        self.checkLineTransparency(self.fig, 1)

    def test_7_color(self):
        self.checkLineColor(self.fig, 'C0')
