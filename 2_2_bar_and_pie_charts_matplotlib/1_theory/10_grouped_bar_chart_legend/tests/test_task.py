from typing import ClassVar, List

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, get_all_regions, get_number_of_decades, get_number_of_regions, preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    aggregated_data: ClassVar[pd.DataFrame]
    regions: ClassVar[List[str]]
    number_of_decades: ClassVar[int]
    number_of_regions: ClassVar[int]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.aggregated_data = aggregate(cls.data)
        cls.regions = get_all_regions(cls.aggregated_data)
        cls.number_of_decades = get_number_of_decades(cls.aggregated_data)
        cls.number_of_regions = get_number_of_regions(cls.aggregated_data)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], self.number_of_regions)
        for i in range(self.number_of_regions):
            self.checkContainerType(self.fig.axes[0], BarContainer, container_number=i)
            self.checkNumberOfBars(self.fig.axes[0], self.aggregated_data["decade"].nunique(), container_number=i)

    def test_2_1_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="vertical")

    def test_2_2_bar_values(self):
        for i, region in enumerate(self.regions):
            expected_values = self.aggregated_data[self.aggregated_data["region"] == region]["sales"].to_list()
            self.checkBarValues(self.fig.axes[0], expected_values, container_number=i)

    def test_2_3_bar_width(self):
        for i in range(self.number_of_regions):
            self.checkBarWidth(self.fig.axes[0], 1, container_number=i)

    def test_2_4_bar_positions(self):
        for i in range(self.number_of_regions):
            self.checkBarPositions(
                self.fig.axes[0],
                list(
                    range(
                        i,
                        self.number_of_decades * (self.number_of_regions + 1),
                        self.number_of_regions + 1,
                    ),
                ),
                container_number=i,
                width=1,
                axis="x",
            )

    def test_2_5_bar_legend(self):
        self.checkLegendExists(self.fig.axes[0])
        self.checkLegendLabels(self.fig.axes[0], expected_labels=list(self.regions))

    def test_3_title(self):
        self.checkTitle(self.fig.axes[0], None)
