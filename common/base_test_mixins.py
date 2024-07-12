from typing import List, Any, Optional
from unittest import TestCase

import matplotlib.pyplot as plt
from matplotlib.colors import same_color, to_rgb
from numpy.testing import assert_allclose, assert_array_almost_equal


class BaseTestMixin(TestCase):
    def checkReturnType(self, obj: Any, expected_type: Any, expected_function: Optional[str] = None):
        error_message = "The return type is wrong."

        if expected_function is not None:
            error_message += f" Please use`{expected_function}`."

        self.assertIsInstance(obj, expected_type, error_message)

    def checkNumberOfAxes(self, axes: List[plt.Axes], expected_number: int):
        self.assertEqual(
            expected_number,
            len(axes),
            f"The figure must have only {expected_number} axes.",
        )

    def checkNumberOfCollections(self, ax: plt.Axes, expected_number: int):
        collections = getattr(ax, "collections", [])
        self.assertEqual(
            expected_number,
            len(collections),
            f"The figure must have only {expected_number} collections.",
        )

    @staticmethod
    def checkCollectionPosition(
        ax: plt.Axes,
        expected_x: List[float],
        expected_y: List[float],
        collection_number: int = 0,
    ):
        actual_x, actual_y = ax.collections[collection_number].get_offsets().T

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
    def checkCollectionTransparency(ax: plt.Axes, expected_transparency: float, collection_number: int = 0):
        if expected_transparency == 1:
            error_message = "The collection must not be transparent."
        else:
            error_message = "The collection must have transparency."

        assert_allclose(ax.collections[collection_number].get_alpha(), expected_transparency, err_msg=error_message)

    def checkCollectionColor(self, ax: plt.Axes, expected_facecolor: str, collection_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_facecolor), to_rgb(ax.collections[collection_number].get_facecolor())),
            msg=f"The collection must be colored with '{expected_facecolor}'.",
        )

    def checkNumberOfLines(self, ax: plt.Axes, expected_number: int):
        lines = getattr(ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            f"The figure must have only {expected_number} lines.",
        )

    @staticmethod
    def checkLinePosition(ax: plt.Axes, expected_x: List[float], expected_y: List[float], line_number: int = 0):
        actual_x, actual_y = ax.lines[line_number].get_xydata().T

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
    def checkLineTransparency(ax: plt.Axes, expected_transparency: float, line_number: int = 0):
        actual_transparency = ax.lines[line_number].get_alpha()
        if actual_transparency is None:
            # If alpha is None, then it by default equals 1
            actual_transparency = 1

        if expected_transparency == 1:
            error_message = "The line must not be transparent."
        else:
            error_message = "The line must have transparency."

        assert_allclose(actual_transparency, expected_transparency, err_msg=error_message)

    def checkLineColor(self, ax: plt.Axes, expected_color: str, line_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_color), to_rgb(ax.lines[line_number].get_color())),
            msg=f"The line must be colored with '{expected_color}'.",
        )
