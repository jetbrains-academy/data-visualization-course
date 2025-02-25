from typing import ClassVar

import numpy as np
from matplotlib.container import BarContainer
import pandas as pd
import seaborn as sns

from test_framework import AxisTestMixin, HistTestMixin

from data import preprocess, read, filter_by_global_sales
from task import plot


class PlotTestCase(HistTestMixin, AxisTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.fig = plot(data)
        cls.data = filter_by_global_sales(data)
        cls.counts, cls.bins = np.histogram(cls.data["global_sales"], bins="auto")

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.displot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_displot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=0)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)

        # Bars
        self.checkNumberOfContainers(self.fig.ax, expected_number=1)
        self.checkContainerType(self.fig.ax, expected_type=BarContainer)
        self.checkNumberOfBars(self.fig.ax, expected_number=len(self.counts))

    def test_2_1_bar_height(self):
        self.checkBarHeights(self.fig.ax, expected_values=self.counts.tolist())

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.ax, expected_layout="vertical")
