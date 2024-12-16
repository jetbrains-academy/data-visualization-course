from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import get_categories_sorted, get_category_products, get_category_votes, read
from task import plot


class TestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()
        cls.fig = plot(data)
        cls.data = data
        cls.sorted_categories = get_categories_sorted()

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure, expected_function="plt.barh")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        self.checkNumberOfContainers(self.fig.axes[0], 3)
        self.checkContainerType(self.fig.axes[0], BarContainer)
        for container in self.fig.axes[0].containers:
            self.assertEqual(
                len(container.datavalues),
                5,
                "Each container must have exactly 5 bars.",
            )

    # TODO: Add test for bars positions
    def test_2_1_bar_position(self):
        for index in range(3):
            expected_positions = get_category_votes(self.data, self.sorted_categories[index])
            self.checkBarsPosition(self.fig.axes[0], expected_positions, container_number=index)

    def test_2_2_bar_layout(self):
        self.checkBarsLayout(self.fig.axes[0], expected_layout="horizontal")

    def test_2_3_bar_labels(self):
        all_labels = []
        for category in self.sorted_categories:
            all_labels.extend(get_category_products(self.data, category))
        self.checkTickLabels(self.fig.axes[0], all_labels, axis="y")

    def test_2_4_bar_colors(self):
        expected_colors = []
        for color in ["green", "firebrick", "navy"]:
            expected_colors.extend([color] * 5)
        self.checkBarsColor(self.fig.axes[0], expected_facecolors=expected_colors)

    def test_3_1_labels(self):
        self.checkLabel(self.fig.axes[0], "Respondents, %", "x")

    def test_3_2_x_lim(self):
        self.checkLim(self.fig.axes[0], [0, 100], "x")

    def test_3_3_x_ticks(self):
        self.checkTicks(self.fig.axes[0], [], "x")

    def test_3_4_y_ticks(self):
        expected_positions = list(range(15))
        expected_labels = []
        for category in self.sorted_categories:
            expected_labels.extend(get_category_products(self.data, category))
        self.checkTicks(self.fig.axes[0], expected_positions, "y")
        self.checkTickLabels(self.fig.axes[0], expected_labels, "y")

    def test_4_title(self):
        self.checkTitle(self.fig.axes[0], "Respondents, %")
