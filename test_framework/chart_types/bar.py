from typing import Literal, Optional, Union

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

    def checkBarValues(self, ax: plt.Axes, *, expected_values: list[float], container_number: int = 0):
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
        expected_position: list[float],
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
        expected_facecolors: Union[Optional[list[ColorName]], ColorName],
        container_number: int = 0,
        histtype: Literal["bar", "step"] = "bar",
    ):
        if histtype == "step":
            actual_facecolor = to_rgb(ax.patches[container_number].get_facecolor())

            if isinstance(expected_facecolors, list):
                raise ValueError("Pass a single color for a step histogram.")

            self.assertSingleColor(
                expected_facecolors,
                actual_facecolor,
                msg=(
                    f"The histogram must be colored in <samp>{expected_facecolors}</samp>, "
                    f"but got <samp>{self._rgb_to_name(actual_facecolor)}</samp>."
                ),
            )
        elif histtype == "bar":
            actual_colors = [to_rgb(bar.get_facecolor()) for bar in ax.containers[container_number]]

            if isinstance(expected_facecolors, ColorName):
                expected_facecolors = [expected_facecolors] * len(actual_colors)

            self.assertColorList(
                expected_facecolors,
                actual_colors,
                msg="The expected bar colors do not match the actual ones.",
            )
        else:
            raise ValueError("Unknown histtype parameter.")
