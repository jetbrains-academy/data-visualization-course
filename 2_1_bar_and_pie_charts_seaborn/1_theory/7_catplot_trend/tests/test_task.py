from typing import ClassVar

from matplotlib.container import BarContainer
import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import preprocess, read, add_decades
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
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.catplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, 1)

    def test_1_3_catplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, 0)
        self.checkNumberOfLines(self.fig.ax, 0)  # Error bars

        number_of_decades = add_decades(self.data)['decade'].nunique()

        # Bars
        self.checkNumberOfContainers(self.fig.ax, 1)
        self.checkContainerType(self.fig.ax, BarContainer)
        self.checkNumberOfBars(self.fig.ax, number_of_decades)

    def test_2_1_bar_position(self):
        data = add_decades(self.data)
        self.checkBarsPosition(self.fig.ax, data.groupby("decade", observed=True)["global_sales"].sum().to_list())

    def test_2_2_bar_layout(self):
        self.checkBarsLayout(self.fig.ax, expected_layout="vertical")

    def test_2_3_bar_labels(self):
        self.checkTickLabels(
            self.fig.ax,
            list(map(str, add_decades(self.data)['decade'].cat.categories)),
            axis="x",
        )
