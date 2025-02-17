from typing import ClassVar, List

from matplotlib.container import BarContainer
import pandas as pd
import seaborn as sns

from common.base_test_mixins import BaseTestMixin
from data import add_decades, extract_sales_region, get_sorted_regions, preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[sns.FacetGrid]

    sorted_regions: ClassVar[List[str]]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.data = add_decades(cls.data)
        cls.data = extract_sales_region(cls.data)

        cls.sorted_regions = get_sorted_regions(cls.data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=sns.FacetGrid, expected_function="sns.catplot")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes.flat, expected_number=1)

    def test_1_3_catplot_kind(self):
        self.checkNumberOfCollections(self.fig.ax, expected_number=0)
        self.checkNumberOfLines(self.fig.ax, expected_number=0)  # Error bars

        number_of_decades = self.data["decade"].nunique()
        number_of_regions = self.data["region"].nunique()

        # Bars
        self.checkNumberOfContainers(self.fig.ax, expected_number=number_of_regions)
        for i in range(number_of_regions):
            self.checkContainerType(self.fig.ax, expected_type=BarContainer, container_number=i)
            self.checkNumberOfBars(self.fig.ax, expected_number=number_of_decades, container_number=i)

    def test_2_1_bar_position(self):
        for i, region in enumerate(self.sorted_regions):
            self.checkBarValues(
                self.fig.ax,
                expected_values=self.data[self.data["region"] == region].groupby("decade", observed=True)["sales"].sum().to_list(),
                container_number=i,
            )

    def test_2_2_bar_layout(self):
        self.checkBarLayout(self.fig.ax, expected_layout="vertical")

    def test_2_3_bar_labels(self):
        self.checkTickLabels(
            self.fig.ax,
            expected_tick_labels=list(map(str, self.data["decade"].cat.categories)),
            axis="x",
        )
