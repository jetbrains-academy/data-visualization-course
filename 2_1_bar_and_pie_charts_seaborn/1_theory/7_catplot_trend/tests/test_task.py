from typing import ClassVar

from matplotlib.container import BarContainer
import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import add_decades, preprocess, read
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

        cls.data = add_decades(data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.catplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_catplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=0)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)  # Error bars

        number_of_decades = self.data["decade"].nunique()

        # Bars
        self.checkNumberOfContainers(self.fig.ax, expected_number=1)
        self.checkContainerType(self.fig.ax, BarContainer)
        self.checkNumberOfBars(self.fig.ax, number_of_decades)

    def test_2_1_bar_position(self):
        self.checkBarValues(self.fig.ax, self.data.groupby("decade", observed=True)["global_sales"].sum().to_list())

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.ax, expected_layout="vertical")

    def test_2_3_bar_labels(self):
        self.checkTickLabels(
            self.fig.ax,
            expected_tick_labels=list(map(str, self.data["decade"].cat.categories)),
            axis="x",
        )
