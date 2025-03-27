from typing import Literal

from matplotlib import pyplot as plt
import numpy as np

from test_framework.base import BaseTestMixin


class OrthogonalLineTestMixin(BaseTestMixin):
    def checkOrthogonalLineCoordinate(
        self,
        ax: plt.Axes,
        *,
        expected_type: Literal["vertical", "horizontal"],
        expected_coordinate: list[float],
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
                f"The expected coordinate value is <samp>{expected_coordinate}</samp>, "
                f"but got <samp>{actual_coordinate[0]}</samp>."
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

        self.assertAlmostEqual(
            expected_width,
            actual_width,
            msg=(f"The expected line width is <samp>{expected_width}</samp>, but got <samp>{actual_width}</samp>."),
        )
