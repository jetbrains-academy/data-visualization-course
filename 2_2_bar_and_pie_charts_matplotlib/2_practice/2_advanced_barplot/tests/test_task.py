from typing import ClassVar

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import pandas as pd

from test_framework import AxisTestMixin, BarTestMixin, FigureTestMixin, LegendTestMixin, TextTestMixin, TitleTestMixin

from data import get_categories, get_category_product_names, get_category_size, get_category_votes, preprocess, read
import task
from task import plot


class TestCase(BarTestMixin, AxisTestMixin, TitleTestMixin, LegendTestMixin, TextTestMixin, FigureTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    categories: ClassVar[list[str]]
    category_colors: ClassVar[dict[str, str]]

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
            self.checkBarValues(self.fig.axes[0], expected_values=expected_positions, container_number=i)

    def test_2_2_bar_position(self):
        offset = 0
        for i, category in enumerate(self.categories):
            category_size = get_category_size(self.data, category)

            self.checkBarPosition(
                self.fig.axes[0],
                expected_position=list(range(offset, offset + category_size)),
                axis="y",
                container_number=i,
            )

            offset += category_size

    def test_2_3_bar_colors(self):
        for i, (_, color) in enumerate(self.category_colors.items()):
            self.checkBarColor(self.fig.axes[0], expected_facecolors=color, container_number=i)

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

    def test_4_1_x_major_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=list(range(0, 101, 25)), axis="x")
        self.checkTickLabels(self.fig.axes[0], expected_tick_labels=list(map(str, range(0, 101, 25))), axis="x")
        self.checkTickLabels(
            self.fig.axes[0],
            expected_tick_labels=list(map(str, range(0, 101, 25))),
            axis="x",
            where="secondary",
        )

    def test_4_2_x_minor_ticks(self):
        expected_positions = [x for x in range(0, 101, 5) if x not in range(0, 101, 25)]

        self.checkTicks(self.fig.axes[0], expected_ticks=expected_positions, axis="x", minor=True)
        self.checkTickLabels(
            self.fig.axes[0],
            expected_tick_labels=[""] * len(expected_positions),
            axis="x",
            minor=True,
        )
        self.checkTickLabels(
            self.fig.axes[0],
            expected_tick_labels=[""] * len(expected_positions),
            axis="x",
            minor=True,
            where="secondary",
        )

    def test_4_3_x_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="Respondents, %", axis="x")

    def test_5_title(self):
        self.checkTitle(self.fig.axes[0], expected_title="Distribution of votes per category")

    def test_6_1_number_of_text_objects(self):
        self.checkNumberOfTextObjects(self.fig.axes[0], expected_number=18)

    def test_6_2_text_values(self):
        expected_x = []
        expected_text = []

        for category in self.categories:
            expected_votes = list(reversed(get_category_votes(self.data, category)))
            expected_x.extend(vote + 1 for vote in expected_votes)
            expected_text.extend(f"{round(vote, 1)}" for vote in expected_votes)

        expected_y = list(range(self.data["product"].nunique()))

        self.checkTextObjects(self.fig.axes[0], expected_texts=list(zip(expected_x, expected_y, expected_text)))

    def test_7_1_legend(self):
        self.checkLegendExists(self.fig.axes[0])

    def test_7_2_legend_number_of_items(self):
        self.checkNumberOfLegendItems(self.fig.axes[0], expected_number=len(self.categories))

    def test_7_3_legend_items(self):
        self.checkLegendLabels(self.fig.axes[0], expected_labels=list(reversed(self.category_colors.keys())))

        self.checkLegendHandleColors(
            self.fig.axes[0],
            expected_handle_colors=list(reversed(self.category_colors.values())),
        )

    def test_8_figure_tight_layout(self):
        self.checkTightLayout(plot_module=task, data=self.data)
