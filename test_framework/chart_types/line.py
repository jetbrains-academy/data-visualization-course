from typing import Optional

from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin, ColorName


class LineTestMixin(BaseTestMixin):
    def checkLinePosition(
        self,
        ax: plt.Axes,
        *,
        expected_x: list[float],
        expected_y: list[float],
        line_number: int = 0,
    ):
        actual_x, actual_y = ax.lines[line_number].get_xydata().T

        self.assertAllClose(
            expected_x,
            actual_x,
            msg=(
                "The expected x-axis values do not match the actual values. "
                "Check that you pass correct x-column to the plotting function."
            ),
        )

        self.assertAllClose(
            expected_y,
            actual_y,
            msg=(
                "The expected y-axis values do not match the actual values. "
                "Check that you pass correct y-column to the plotting function."
            ),
        )

    def checkLineTransparency(self, ax: plt.Axes, *, expected_alpha: float, line_number: int = 0):
        actual_alpha = ax.lines[line_number].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = f"The line must not be transparent, but got <samp>{actual_alpha}</samp>."
        else:
            error_message = (
                f"The line must have transparency equal to <samp>{expected_alpha}</samp>, "
                f"but got <samp>{actual_alpha}</samp>."
            )

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkLineColor(self, ax: plt.Axes, *, expected_color: Optional[ColorName], line_number: int = 0):
        actual_color = to_rgb(ax.lines[line_number].get_color())

        self.assertSingleColor(
            expected_color,
            actual_color,
            msg=(
                f"The line must be colored in <samp>{expected_color}</samp>, "
                f"but got <samp>{self._rgb_to_name(actual_color)}</samp>."
            ),
        )
