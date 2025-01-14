from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, get_number_of_decades, preprocess, read
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
        cls.ordered_regions = ["other", "jp", "na", "eu"]
        cls.number_of_regions = len(cls.ordered_regions)

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure, expected_function="plt.bar")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        aggregated_data = aggregate(self.data)

        # Bars
        self.checkNumberOfContainers(self.fig.axes[0], 4)
        for i in range(len(self.ordered_regions)):
            self.checkContainerType(self.fig.axes[0], BarContainer, container_number=i)
            self.checkNumberOfBars(self.fig.axes[0], aggregated_data["decade"].nunique(), container_number=i)

    def test_2_1_bar_values(self):
        aggregated_data = aggregate(self.data)

        for i, region in enumerate(self.ordered_regions):
            expected_values = aggregated_data[aggregated_data["region"] == region]["sales"].to_list()
            self.checkBarValues(self.fig.axes[0], expected_values, container_number=i)

    def test_2_2_bar_width(self):
        aggregated_data = aggregate(self.data)

        for i in range(len(self.ordered_regions)):
            self.checkBarWidth(self.fig.axes[0], 1, container_number=i)

    def test_2_3_bar_positions(self):
        aggregated_data = aggregate(self.data)

        for i in range(len(self.ordered_regions)):
            self.checkBarPositions(
                self.fig.axes[0],
                list(
                    range(
                        i,
                        get_number_of_decades(aggregated_data) * (self.number_of_regions + 1),
                        self.number_of_regions + 1,
                    ),
                ),
                container_number=i,
                width=1,
                axis="x")

        def test_2_4_bar_layout(self):
            self.checkBarLayout(self.fig.axes[0], expected_layout="vertical")
