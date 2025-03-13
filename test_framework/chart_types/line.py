from typing import List, Optional, Union, Literal

from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt
import numpy as np

from test_framework.base import BaseTestMixin, ColorName


class LineTestMixin(BaseTestMixin):
    def checkLinePosition(
        self,
        ax: plt.Axes,
        *,
        expected_x: List[float],
        expected_y: List[float],
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

    def checkOrthogonalLineCoordinate(
        self,
        ax: plt.Axes,
        *,
        expected_type: Literal["vertical", "horizontal"],
        expected_coordinate: Union[List[float], List[int]],
        line_number: int = 0,
    ):
        if expected_type == "vertical":
            actual_coordinate = ax.lines[line_number].get_xydata().T[0]
        elif expected_type == "horizontal":
            actual_coordinate = ax.lines[line_number].get_xydata().T[1]
        else:
            raise ValueError("Unknown expected_type parameter.")

        self.assertTrue(np.unique(actual_coordinate).size == 1, f"The line must be {expected_type}.")

        self.assertAlmostEqual(
            expected_coordinate,
            actual_coordinate[0],
            msg=(
                f"The expected coordinate value is <samp>{expected_coordinate}</samp>, but got <samp>{actual_coordinate[0]}</samp>."
            ),
        )

    def checkOrthogonalLineStyle(self, ax: plt.Axes, *, expected_style: str, line_number: int = 0):
        actual_style = ax.lines[line_number].get_linestyle()

        self.assertEqual(
            expected_style,
            actual_style,
            msg=(f"The expected line style is <samp>{expected_style}</samp>, but got <samp>{actual_style}</samp>."),
        )

    def checkOrthogonalLineWidth(self, ax: plt.Axes, *, expected_width: float, line_number: int = 0):
        actual_width = ax.lines[line_number].get_linewidth()

        self.assertEqual(
            expected_width,
            actual_width,
            msg=(f"The expected line width is <samp>{expected_width}</samp>, but got <samp>{actual_width}</samp>."),
        )
