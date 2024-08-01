from typing import Any, List, Literal, Optional
from unittest import TestCase

from matplotlib.colors import same_color, to_rgb
import matplotlib.pyplot as plt
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
            error_message = f"The collection must have transparency ({expected_transparency})."

        actual_alpha = ax.collections[collection_number].get_alpha()
        if actual_alpha is None:
            actual_alpha = 1

        assert_allclose(actual_alpha, expected_transparency, err_msg=error_message)

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

    def checkLim(self, ax: plt.Axes, expected_lim: List[float], axis: Literal["x", "y"]):
        if axis == "x":
            actual_lim = ax.get_xlim()
        elif axis == "y":
            actual_lim = ax.get_ylim()
        else:
            raise ValueError("Unknown axis name.")

        assert_array_almost_equal(
            actual_lim,
            expected_lim,
            err_msg=f"The figure should be limited from {expected_lim[0]} to {expected_lim[1]} for {axis}-axis.",
        )

    def checkLabel(self, ax: plt.Axes, expected_label: Optional[str], axis: Literal["x", "y"]):
        if axis == "x":
            actual_label = ax.get_xlabel()
        elif axis == "y":
            actual_label = ax.get_ylabel()
        else:
            raise ValueError("Unknown axis name.")

        if expected_label is None:
            self.assertEqual("", actual_label, f"The {axis}-axis should have no labels")
            return

        self.assertEqual(
            actual_label,
            expected_label,
            f"The {axis}-axis should have the following label: '{expected_label}'",
        )

    def checkTicks(self, ax: plt.Axes, expected_ticks: List[float], axis: Literal["x", "y"], *, minor: bool = False):
        if axis == "x":
            actual_ticks = ax.get_xticks(minor=minor)
        elif axis == "y":
            actual_ticks = ax.get_yticks(minor=minor)
        else:
            raise ValueError("Unknown axis name.")

        assert_array_almost_equal(
            actual_ticks,
            expected_ticks,
            err_msg=f"The expected {axis}-axis tick values do not match the actual values. "
            f"Check that you pass the correct values to the `set_{axis}ticks` function.",
        )

    def checkSpineVisibility(
        self,
        ax: plt.Axes,
        position: Literal["left", "right", "top", "bottom"],
        *,
        expected_visibility: bool,
    ):
        actual_visibility = ax.spines[position].get_visible()

        if expected_visibility:
            error_message = f"The {position} spine must be visible."
        else:
            error_message = f"The {position} spine must not be visible."

        self.assertEqual(actual_visibility, expected_visibility, msg=error_message)
