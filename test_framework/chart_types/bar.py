from typing import List, Literal, Optional

from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin, ColorName


class BarTestMixin(BaseTestMixin):
    def checkNumberOfBars(self, ax: plt.Axes, *, expected_number: int, container_number: int = 0):
        datavalues = ax.containers[container_number].datavalues

        self.assertEqual(
            expected_number,
            len(datavalues),
            f"The figure must have only <samp>{expected_number}</samp> bars.",
        )

    def checkBarValues(self, ax: plt.Axes, *, expected_values: List[float], container_number: int = 0):
        actual_position = ax.containers[container_number].datavalues

        self.assertAllClose(
            expected_values,
            actual_position,
            msg="The expected bar values do not match the actual values.",
        )

    def checkBarWidth(self, ax: plt.Axes, *, expected_width: float, container_number: int = 0):
        actual_widths = [bar.get_width() for bar in ax.containers[container_number]]
        expected_widths = [expected_width] * len(actual_widths)

        self.assertAllClose(
            expected_widths,
            actual_widths,
            msg="The expected bar widths do not match the actual widths.",
        )

    def checkBarPosition(
        self,
        ax: plt.Axes,
        *,
        expected_position: List[float],
        width: float = 0.8,
        axis: Literal["x", "y"],
        container_number: int = 0,
    ):
        if axis == "x":
            actual_positions = [bar.get_x() + width / 2 for bar in ax.containers[container_number]]
        elif axis == "y":
            actual_positions = [bar.get_y() + width / 2 for bar in ax.containers[container_number]]
        else:
            raise ValueError("Unknown axis name.")

        self.assertAllClose(
            expected_position,
            actual_positions,
            msg=f"The actual position of the bars in container #{container_number} does not match the expected one.",
        )

    def checkBarLayout(
        self,
        ax: plt.Axes,
        *,
        expected_layout: Literal["horizontal", "vertical"],
        container_number: int = 0,
    ):
        actual_layout = ax.containers[container_number].orientation
        if actual_layout is None:
            self.fail("The bars must be placed either horizontally or vertically.")

        self.assertEqual(
            expected_layout,
            actual_layout,
            f"The bars must be oriented in the <samp>{expected_layout}</samp> direction.",
        )

    def checkBarColor(
        self,
        ax: plt.Axes,
        *,
        expected_facecolors: Optional[List[ColorName]],
        container_number: int = 0,
    ):
        actual_colors = [to_rgb(bar.get_facecolor()) for bar in ax.containers[container_number]]

        self.assertColorList(
            expected_facecolors,
            actual_colors,
            msg="The expected bar colors do not match the actual ones.",
        )
