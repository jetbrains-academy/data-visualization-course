from typing import ClassVar, Dict, List

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import get_categories, get_category_product_names, get_category_size, get_category_votes, preprocess, read
from task import plot


class TestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    categories: ClassVar[List[str]]
    category_colors: ClassVar[Dict[str, str]]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.fig = plot(data)
        cls.data = data

        cls.categories = list(reversed(get_categories(cls.data)))

        cls.category_colors = {
            "salad": "forestgreen",
            "cheese": "goldenrod",
            "bread": "sienna",
        }

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        self.checkNumberOfContainers(self.fig.axes[0], expected_number=3)
        for i in range(3):
            self.checkContainerType(self.fig.axes[0], expected_type=BarContainer, container_number=i)

    def test_1_4_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="horizontal")

    def test_2_1_bar_values(self):
        for i, category in enumerate(self.categories):
            expected_positions = list(reversed(get_category_votes(self.data, category)))
            self.checkBarValues(self.fig.axes[0], expected_positions, container_number=i)

    def test_2_2_bar_position(self):
        offset = 0
        for i, category in enumerate(self.categories):
            category_size = get_category_size(self.data, category)

            self.checkBarPositions(
                self.fig.axes[0],
                list(range(offset, offset + category_size)),
                axis="y",
                container_number=i,
            )

            offset += category_size

    def test_2_3_bar_colors(self):
        for i, (category, color) in enumerate(self.category_colors.items()):
            expected_colors = [color] * get_category_size(self.data, category)
            self.checkBarColor(self.fig.axes[0], expected_facecolors=expected_colors, container_number=i)

    def test_3_1_y_ticks(self):
        expected_labels = []
        number_of_products = 0
        for category in self.categories:
            expected_labels.extend(reversed(get_category_product_names(self.data, category)))
            number_of_products += get_category_size(self.data, category)

        self.checkTicks(self.fig.axes[0], expected_ticks=list(range(number_of_products)), axis="y")
        self.checkTickLabels(self.fig.axes[0], expected_tick_labels=expected_labels, axis="y")

    def test_3_2_y_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="Product name", axis="y")

    def test_4_1_x_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=list(range(0, 101, 25)), axis="x")
        self.checkTickLabels(self.fig.axes[0], expected_tick_labels=list(map(str, range(0, 101, 25))), axis="x")

    def test_4_2_x_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="Respondents, %", axis="x")

    def test_5_title(self):
        self.checkTitle(self.fig.axes[0], expected_title="Distribution of votes per category")

    def test_6_1_legend_exists(self):
        self.checkLegendExists(self.fig.axes[0])

    def test_6_2_legend_number_of_items(self):
        self.checkNumberOfLegendItems(self.fig.axes[0], expected_number=len(self.categories))

    def test_6_3_legend_labels(self):
        self.checkLegendLabels(self.fig.axes[0], expected_labels=self.categories)

    def test_6_4_legend_handle_colors(self):
        self.checkLegendHandleColors(self.fig.axes[0], expected_handle_colors=list(self.category_colors.values()))
