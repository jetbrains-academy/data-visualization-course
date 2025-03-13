from typing import ClassVar

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from test_framework import (
    AxisTestMixin,
    CollectionTestMixin,
    FigureTestMixin,
    HistTestMixin,
    LegendTestMixin,
    LineTestMixin,
    SpineTestMixin,
    TextTestMixin,
    TitleTestMixin,
)

from data import get_bins, get_city_sales, get_weights, read
from task import plot


class PlotTestCase(
    HistTestMixin,
    AxisTestMixin,
    LegendTestMixin,
    TitleTestMixin,
    TextTestMixin,
    CollectionTestMixin,
    SpineTestMixin,
    FigureTestMixin,
    LineTestMixin,
):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]
    bins: ClassVar[np.ndarray]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)
        cls.cities = ["Yerevan", "Belgrade"]
        cls.bins = get_bins(data)
        cls.color_map = {
            "Yerevan": "pink",
            "Belgrade": "grey",
        }
        cls.edge_color_map = {
            "Yerevan": "crimson",
            "Belgrade": "black",
        }
        cls.y_coordinates_scatter = {
            "Yerevan": 0.1,
            "Belgrade": 0.2,
        }
        cls.sign_map = {
            "Yerevan": -1,
            "Belgrade": 1,
        }
        cls.position_map = {
            "Yerevan": "right",
            "Belgrade": "left",
        }

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=2)

    def test_1_3_scatter_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=2)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=0)

        self.checkNumberOfContainers(self.fig.axes[0], expected_number=0)
        self.checkNumberOfPatches(self.fig.axes[0], expected_number=0)

    def test_1_4_plot_kind(self):
        self.checkNumberOfCollections(self.fig.axes[1], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[1], expected_number=2)

        self.checkNumberOfContainers(self.fig.axes[1], expected_number=0)
        self.checkNumberOfPatches(self.fig.axes[1], expected_number=2)
        self.checkNumberOfTextObjects(self.fig.axes[1], expected_number=2)
        for patch_number in range(len(self.cities)):
            self.checkPatchType(self.fig.axes[1], expected_type=Polygon, patch_number=patch_number)

    def test_1_5_figure_height_ratio(self):
        self.checkHeightRatio(self.fig.axes[0], expected_ratio=[1, 10])

    def test_2_1_scatter_positions(self):
        for collection_number, city in enumerate(self.cities):
            city_sales = get_city_sales(self.data, city)
            self.checkCollectionPosition(
                self.fig.axes[0],
                expected_x=city_sales.tolist(),
                expected_y=[self.y_coordinates_scatter[city]] * len(city_sales),
                collection_number=collection_number,
            )

    def test_2_2_scatter_transparency(self):
        for collection_number in range(len(self.cities)):
            self.checkCollectionTransparency(self.fig.axes[0], expected_alpha=0.1, collection_number=collection_number)

    def test_2_3_scatter_spines(self):
        self.checkSpineVisibility(self.fig.axes[0], position="top", expected_visibility=False)
        self.checkSpineVisibility(self.fig.axes[0], position="bottom", expected_visibility=False)
        self.checkSpineVisibility(self.fig.axes[0], position="left", expected_visibility=False)
        self.checkSpineVisibility(self.fig.axes[0], position="right", expected_visibility=False)

    def test_2_4_scatter_ticks(self):
        self.checkTicks(self.fig.axes[0], axis="x", expected_ticks=[])
        self.checkTicks(self.fig.axes[0], axis="y", expected_ticks=[])

    def test_2_5_scatter_y_limit(self):
        self.checkLim(self.fig.axes[0], expected_lim=(0, 0.3), axis="y")

    def test_2_6_scatter_colors(self):
        for collection_number, city in enumerate(self.cities):
            self.checkCollectionColor(
                self.fig.axes[0],
                expected_facecolor=self.color_map[city],
                collection_number=collection_number,
            )

    def test_3_1_bar_bins(self):
        for patch_number in range(len(self.cities)):
            self.checkBarBins(
                self.fig.axes[1],
                expected_bins=self.bins.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_3_2_bar_height(self):
        for patch_number, city in enumerate(self.cities):
            city_sales = get_city_sales(self.data, city)
            weights = get_weights(city_sales)
            counts, _ = np.histogram(city_sales, bins=self.bins, weights=weights)
            self.checkBarHeights(
                self.fig.axes[1],
                expected_values=counts.tolist(),
                container_number=patch_number,
                histtype="step",
            )

    def test_3_3_bar_transparency(self):
        for patch_number in range(len(self.cities)):
            self.checkBarTransparency(
                self.fig.axes[1],
                expected_alpha=0.5,
                container_number=patch_number,
                histtype="step",
            )

    def test_3_4_bar_legend(self):
        self.checkLegendExists(self.fig.axes[1])
        self.checkLegendLabels(self.fig.axes[1], expected_labels=self.cities)

    def test_4_1_lines_coordinate(self):
        for line_number, city in enumerate(self.cities):
            city_sales = get_city_sales(self.data, city)
            median = city_sales.median()
            self.checkOrthogonalLineCoordinate(
                self.fig.axes[1],
                expected_type="vertical",
                expected_coordinate=median,
                line_number=line_number,
            )

    def test_4_2_lines_style(self):
        for line_number in range(len(self.cities)):
            self.checkOrthogonalLineStyle(self.fig.axes[1], expected_style="--", line_number=line_number)

    def test_4_3_lines_width(self):
        for line_number in range(len(self.cities)):
            self.checkOrthogonalLineWidth(self.fig.axes[1], expected_width=1.5, line_number=line_number)

    def test_4_4_lines_colors(self):
        for line_number, city in enumerate(self.cities):
            self.checkLineColor(self.fig.axes[1], expected_color=self.edge_color_map[city], line_number=line_number)

    def test_5_1_text_objects_number(self):
        self.checkNumberOfTextObjects(self.fig.axes[1], expected_number=2)

    def test_5_2_text_objects(self):
        expected_texts = []
        for city in self.cities:
            city_sales = get_city_sales(self.data, city)
            median = city_sales.median()
            expected_texts.append((median + self.sign_map[city] * 25, 0.005, str(median)))
        self.checkTextObjects(
            self.fig.axes[1],
            expected_texts=expected_texts,
        )

    def test_5_3_text_objects_colors(self):
        for text_number, city in enumerate(self.cities):
            self.checkTextObjectColor(
                self.fig.axes[1],
                expected_color=self.edge_color_map[city],
                text_number=text_number,
            )

    def test_5_4_text_objects_horizontal_alignment(self):
        for text_number, city in enumerate(self.cities):
            self.checkTextObjectHorizontalAlignment(
                self.fig.axes[1],
                expected_alignment=self.position_map[city],
                text_number=text_number,
            )

    def test_6_1_bar_colors(self):
        for patch_number, city in enumerate(self.cities):
            self.checkStepHistColor(
                self.fig.axes[1],
                expected_facecolor=self.color_map[city],
                container_number=patch_number,
            )

    def test_6_2_bar_edge_colors(self):
        for patch_number, city in enumerate(self.cities):
            self.checkStepHistEdgeColor(
                self.fig.axes[1],
                expected_edgecolor=self.edge_color_map[city],
                container_number=patch_number,
            )

    def test_7_labels(self):
        self.checkLabel(self.fig.axes[1], expected_label="Sales", axis="x")
        self.checkLabel(self.fig.axes[1], expected_label="Probability", axis="y")
