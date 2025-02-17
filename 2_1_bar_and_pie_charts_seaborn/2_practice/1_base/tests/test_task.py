from typing import ClassVar

from matplotlib.container import BarContainer
import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import get_product_order, read
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
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.catplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_catplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=0)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)

        # Bars
        self.checkNumberOfContainers(self.fig.ax, expected_number=self.data["category"].nunique())
        for i, category in enumerate(self.data["category"].unique()):
            self.checkContainerType(self.fig.ax, expected_type=BarContainer, container_number=i)

            self.checkNumberOfBars(
                self.fig.ax,
                expected_number=self.data[self.data["category"] == category]["product"].nunique(),
                container_number=i,
            )

    def test_2_1_bar_layout(self):
        for i in range(self.data["category"].nunique()):
            self.checkBarLayout(self.fig.ax, expected_layout="horizontal", container_number=i)

    def test_2_2_bar_position(self):
        for i, category in enumerate(self.data["category"].unique()):
            expected_values = (
                self.data[self.data["category"] == category].groupby("product", sort=False).size().sort_index()
            )
            self.checkBarValues(self.fig.ax, expected_values.to_list(), container_number=i)

    def test_2_3_bar_labels(self):
        self.checkTickLabels(
            self.fig.ax,
            expected_tick_labels=get_product_order(self.data),
            axis="y",
        )

    def test_3_1_number_of_legend_items(self):
        self.checkNumberOfLegendItems(self.fig, expected_number=self.data["category"].nunique())

    def test_3_2_legend_labels(self):
        self.checkLegendLabels(self.fig, expected_labels=list(self.data["category"].unique()))
