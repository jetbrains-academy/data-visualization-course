from typing import Any, List, Optional
from unittest import TestCase

from matplotlib.colors import same_color, to_rgb
from numpy.testing import assert_allclose, assert_array_almost_equal
from seaborn import FacetGrid


class BaseTestMixin(TestCase):
    def checkReturnType(self, obj: Any, expected_function: Optional[str] = None):
        error_message = "The return type is wrong. Please use "

        if expected_function is None:
            error_message += "a figure-level function."
        else:
            error_message += f"`{expected_function}`."

        self.assertIsInstance(obj, FacetGrid, error_message)

    def checkNumberOfAxes(self, fig: FacetGrid, expected_number: int):
        axes = fig.axes.flat
        self.assertEqual(
            expected_number,
            len(axes),
            f"The figure must have only {expected_number} axes.",
        )

    def checkNumberOfCollections(self, fig: FacetGrid, expected_number: int):
        collections = getattr(fig.ax, "collections", [])
        self.assertEqual(
            expected_number,
            len(collections),
            f"The figure must have only {expected_number} collections.",
        )

    @staticmethod
    def checkCollectionPosition(
        fig: FacetGrid,
        expected_x: List[float],
        expected_y: List[float],
        collection_number: int = 0,
    ):
        actual_x, actual_y = fig.ax.collections[collection_number].get_offsets().T

        assert_array_almost_equal(
            actual_x,
            expected_x,
            err_msg=(
                "The expected x-axis values do not match the actual values. "
                "Check that you pass correct x-column to the plotting function."
            ),
        )

        assert_array_almost_equal(
            actual_y,
            expected_y,
            err_msg=(
                "The expected y-axis values do not match the actual values. "
                "Check that you pass correct y-column to the plotting function."
            ),
        )

    @staticmethod
    def checkCollectionTransparency(fig: FacetGrid, expected_transparency: float, collection_number: int = 0):
        if expected_transparency == 1:
            error_message = "The collection must not be transparent."
        else:
            error_message = "The collection must have transparency."

        assert_allclose(fig.ax.collections[collection_number].get_alpha(), expected_transparency, err_msg=error_message)

    def checkCollectionColor(self, fig: FacetGrid, expected_facecolor: str, collection_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_facecolor), to_rgb(fig.ax.collections[collection_number].get_facecolor())),
            msg=f"The collection must be colored with '{expected_facecolor}'.",
        )

    def checkNumberOfLines(self, fig: FacetGrid, expected_number: int):
        lines = getattr(fig.ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            f"The figure must have only {expected_number} lines.",
        )

    @staticmethod
    def checkLinePosition(fig: FacetGrid, expected_x: List[float], expected_y: List[float], line_number: int = 0):
        actual_x, actual_y = fig.ax.lines[line_number].get_xydata().T

        assert_array_almost_equal(
            actual_x,
            expected_x,
            err_msg=(
                "The expected x-axis values do not match the actual values. "
                "Check that you pass correct x-column to the plotting function."
            ),
        )

        assert_array_almost_equal(
            actual_y,
            expected_y,
            err_msg=(
                "The expected y-axis values do not match the actual values. "
                "Check that you pass correct y-column to the plotting function."
            ),
        )

    @staticmethod
    def checkLineTransparency(fig: FacetGrid, expected_transparency: float, line_number: int = 0):
        actual_transparency = fig.ax.lines[line_number].get_alpha()
        if actual_transparency is None:
            # If alpha is None, then it by default equals 1
            actual_transparency = 1

        if expected_transparency == 1:
            error_message = "The line must not be transparent."
        else:
            error_message = "The line must have transparency."

        assert_allclose(actual_transparency, expected_transparency, err_msg=error_message)

    def checkLineColor(self, fig: FacetGrid, expected_color: str, line_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_color), to_rgb(fig.ax.lines[line_number].get_color())),
            msg=f"The line must be colored with '{expected_color}'.",
        )
