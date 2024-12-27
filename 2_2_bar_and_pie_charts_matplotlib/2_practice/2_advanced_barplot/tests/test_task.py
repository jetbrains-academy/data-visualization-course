from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import get_categories, get_category_product_names, get_category_size, get_category_votes, read, preprocess
from task import plot


class TestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.fig = plot(data)
        cls.data = data

        cls.category_colors = {
            "bread": "sienna",
            "cheese": "goldenrod",
            "salad": "forestgreen",
        }

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure, expected_function="plt.barh")

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, 1)

    def test_1_3_bar_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], 0)
        self.checkNumberOfLines(self.fig.axes[0], 0)

        self.checkNumberOfContainers(self.fig.axes[0], 3)
        for i in range(3):
            self.checkContainerType(self.fig.axes[0], BarContainer, container_number=i)

    def test_1_4_bar_layout(self):
        self.checkBarLayout(self.fig.axes[0], expected_layout="horizontal")

    def test_2_1_bar_values(self):
        for i, category in enumerate(get_categories(self.data)):
            expected_positions = get_category_votes(self.data, category)
            self.checkBarValues(self.fig.axes[0], expected_positions, container_number=i)

    def test_2_2_bar_position(self):
        offset = 0
        for i, category in enumerate(get_categories(self.data)):
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
        for category in get_categories(self.data):
            expected_labels.extend(get_category_product_names(self.data, category))
            number_of_products += get_category_size(self.data, category)

        self.checkTicks(self.fig.axes[0], list(range(number_of_products)), axis="y")
        self.checkTickLabels(self.fig.axes[0], expected_labels, axis="y")

    def test_3_2_y_label(self):
        self.checkLabel(self.fig.axes[0], "Product name", axis="y")

    def test_4_1_x_lim(self):
        self.checkLim(self.fig.axes[0], [0, 100], "x")

    def test_4_2_x_major_ticks(self):
        self.checkTicks(self.fig.axes[0], list(range(0, 101, 25)), axis="x")
        self.checkTickLabels(self.fig.axes[0], list(map(str, range(0, 101, 25))), axis="x")
        self.checkTickLabels(self.fig.axes[0], list(map(str, range(0, 101, 25))), axis="x", where="secondary")

    def test_4_3_x_minor_ticks(self):
        expected_positions = [x for x in range(0, 101, 5) if x not in range(0, 101, 25)]

        self.checkTicks(self.fig.axes[0], expected_positions, axis="x", minor=True)
        self.checkTickLabels(self.fig.axes[0], [""] * len(expected_positions), axis="x", minor=True)
        self.checkTickLabels(self.fig.axes[0], [""] * len(expected_positions), axis="x", minor=True, where="secondary")

    def test_4_4_x_label(self):
        self.checkLabel(self.fig.axes[0], "Respondents, %", "x")

    def test_5_title(self):
        self.checkTitle(self.fig.axes[0], "Distribution of votes per category")

    def test_6_1_number_of_text(self):
        self.checkNumberOfTextObjects(self.fig.axes[0], 18)

    def test_6_2_text(self):
        expected_x = (self.data["votes"] + 1).to_list()
        expected_y = list(range(18))
        expected_text = self.data["votes"].apply(lambda x: f"{round(x, 1)}").to_list()
        self.checkTextObjects(self.fig.axes[0], list(zip(expected_x, expected_y, expected_text)))

    def test_7_1_legend(self):
        self.checkLegendExists(self.fig.axes[0])

    def test_7_2_legend_number_of_items(self):
        self.checkNumberOfLegendItems(self.fig.axes[0], expected_number=3)

    def test_7_3_legend_items(self):
        self.checkLegendLabels(self.fig.axes[0], expected_labels=list(reversed(self.category_colors.keys())))

        self.checkLegendHandleColors(
            self.fig.axes[0],
            expected_handle_colors=list(reversed(self.category_colors.values())),
        )
