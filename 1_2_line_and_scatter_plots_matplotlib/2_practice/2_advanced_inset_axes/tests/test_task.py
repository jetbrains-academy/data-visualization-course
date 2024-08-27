from typing import ClassVar

from matplotlib.patches import ConnectionPatch, Rectangle
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    @classmethod
    def setUpClass(cls):
        data = read()

        cls.data = data
        cls.fig = plot(data)

    def test_01_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_01_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_01_3_relplot_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=1)
        self.checkNumberOfLines(self.fig.axes[0], expected_number=1)

    def test_02_1_line_position(self):
        self.checkLinePosition(self.fig.axes[0], expected_x=self.data["x"], expected_y=self.data["approximated_y"])

    def test_02_2_line_color(self):
        self.checkLineColor(self.fig.axes[0], expected_color="navy")

    def test_02_3_line_transparency(self):
        self.checkLineTransparency(self.fig.axes[0], expected_alpha=1)

    def test_03_1_scatter_position(self):
        self.checkCollectionPosition(self.fig.axes[0], expected_x=self.data["x"], expected_y=self.data["y"])

    def test_03_2_scatter_color(self):
        self.checkCollectionColor(self.fig.axes[0], expected_facecolor="grey")

    def test_03_3_scatter_transparency(self):
        self.checkCollectionTransparency(self.fig.axes[0], expected_alpha=0.05)

    def test_04_spines(self):
        self.checkSpineVisibility(self.fig.axes[0], position="top", expected_visibility=False)
        self.checkSpineVisibility(self.fig.axes[0], position="bottom", expected_visibility=True)
        self.checkSpineVisibility(self.fig.axes[0], position="left", expected_visibility=True)
        self.checkSpineVisibility(self.fig.axes[0], position="right", expected_visibility=False)

    def test_05_1_x_lim(self):
        self.checkLim(self.fig.axes[0], expected_lim=[-4, 4], axis="x")

    def test_05_2_x_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=[-4, 0, 4], axis="x")

    def test_05_3_x_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="x", axis="x")

    def test_06_1_y_lim(self):
        self.checkLim(self.fig.axes[0], expected_lim=[-2, 2], axis="y")

    def test_06_2_y_ticks(self):
        self.checkTicks(self.fig.axes[0], expected_ticks=[-1.5, 0, 1.5], axis="y")

    def test_06_3_y_label(self):
        self.checkLabel(self.fig.axes[0], expected_label="y", axis="y")

    def test_07_1_number_of_inset_axes(self):
        self.checkNumberOfAxes(self.fig.axes[0].child_axes, 1)

    def test_07_2_inset_axes_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0].child_axes[0], 1)
        self.checkNumberOfLines(self.fig.axes[0].child_axes[0], 1)

    def test_08_1_inset_axes_line_position(self):
        self.checkLinePosition(
            self.fig.axes[0].child_axes[0],
            expected_x=self.data["x"],
            expected_y=self.data["approximated_y"],
        )

    def test_08_2_inset_axes_line_color(self):
        self.checkLineColor(self.fig.axes[0].child_axes[0], expected_color="navy")

    def test_08_3_inset_axes_line_transparency(self):
        self.checkLineTransparency(self.fig.axes[0].child_axes[0], expected_alpha=1)

    def test_09_1_inset_axes_scatter_position(self):
        self.checkCollectionPosition(
            self.fig.axes[0].child_axes[0],
            expected_x=self.data["x"],
            expected_y=self.data["y"],
        )

    def test_09_2_inset_axes_scatter_color(self):
        self.checkCollectionColor(self.fig.axes[0].child_axes[0], expected_facecolor="grey")

    def test_09_3_inset_axes_scatter_transparency(self):
        self.checkCollectionTransparency(self.fig.axes[0].child_axes[0], expected_alpha=0.05)

    def test_10_1_inset_axes_x_lim(self):
        self.checkLim(self.fig.axes[0].child_axes[0], expected_lim=[0.5, 1.5], axis="x")

    def test_10_2_inset_axes_x_ticks(self):
        self.checkTicks(self.fig.axes[0].child_axes[0], expected_ticks=[0.5, 1.5], axis="x")

    def test_10_3_inset_axes_x_label(self):
        self.checkLabel(self.fig.axes[0].child_axes[0], expected_label=None, axis="x")

    def test_11_1_inset_axes_y_lim(self):
        self.checkLim(self.fig.axes[0].child_axes[0], expected_lim=[0.6, 1.1], axis="y")

    def test_11_2_inset_axes_y_ticks(self):
        self.checkTicks(self.fig.axes[0].child_axes[0], expected_ticks=[0.6, 1.1], axis="y")

    def test_11_3_inset_axes_y_label(self):
        self.checkLabel(self.fig.axes[0].child_axes[0], expected_label=None, axis="y")

    def test_12_1_inset_axes_zoom(self):
        patches = self.fig.axes[0].patches

        self.assertNotEqual(len(patches), 0, "Add an inset zoom")

        rectangles = [patch for patch in patches if isinstance(patch, Rectangle)]
        self.assertEqual(len(rectangles), 1, "There must be exactly one inset zoom")

        connections = [patch for patch in patches if isinstance(patch, ConnectionPatch)]
        self.assertEqual(len(connections), 4, "There must be exactly one inset zoom")

    def test_12_2_inset_axes_zoom_parent_rectangle_position(self):
        rectangle = next(patch for patch in self.fig.axes[0].patches if isinstance(patch, Rectangle))

        actual_x0, actual_y0 = rectangle.get_xy()
        actual_x1 = actual_x0 + rectangle.get_width()
        actual_y1 = actual_y0 + rectangle.get_height()

        self.assertEqual(actual_x0, 0.5, "The inset zoom must must correspond to the area from x = 0.5 to x = 1.5")
        self.assertEqual(actual_x1, 1.5, "The inset zoom must must correspond to the area from x = 0.5 to x = 1.5")
        self.assertEqual(actual_y0, 0.6, "The inset zoom must must correspond to the area from y = 0.6 to y = 1.1")
        self.assertEqual(actual_y1, 1.1, "The inset zoom must must correspond to the area from y = 0.6 to y = 1.1")

    def test_12_3_inset_axes_zoom_parent_connection_positions(self):
        connections = [patch for patch in self.fig.axes[0].patches if isinstance(patch, ConnectionPatch)]

        expected_xys = [(0.5, 0.6), (0.5, 1.1), (1.5, 0.6), (1.5, 1.1)]
        for connection, expected_xy in zip(connections, expected_xys):
            actual_x, actual_y = connection.xy2
            expected_x, expected_y = expected_xy

            self.assertEqual(
                actual_x,
                expected_x,
                "The inset zoom must must correspond to the area from x = 0.5 to x = 1.5",
            )
            self.assertEqual(
                actual_y,
                expected_y,
                "The inset zoom must must correspond to the area from y = 0.6 to y = 1.1",
            )
