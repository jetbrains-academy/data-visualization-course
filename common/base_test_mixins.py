from typing import Any, List, Literal, Optional, Type
from unittest import TestCase

from matplotlib.colors import same_color, to_rgb
from matplotlib.container import Container
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose


class BaseTestMixin(TestCase):
    longMessage = False

    def assertAlmostAllEqual(self, expected: Any, actual: Any, msg: str):
        # The numpy error message is not compatible with the plugin,
        # so we reraise it via unittest appending a custom message
        try:
            assert_allclose(actual, expected)
        except AssertionError as e:
            raise self.failureException(msg + str(e)) from None

    # ----------------------------------------------------------------------

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

    def checkCollectionPosition(
        self,
        ax: plt.Axes,
        expected_x: List[float],
        expected_y: List[float],
        collection_number: int = 0,
    ):
        actual_x, actual_y = ax.collections[collection_number].get_offsets().T

        self.assertAlmostAllEqual(
            expected_x,
            actual_x,
            msg=(
                "The expected x-axis values do not match the actual values. "
                "Check that you pass correct x-column to the plotting function."
            ),
        )

        self.assertAlmostAllEqual(
            expected_y,
            actual_y,
            msg=(
                "The expected y-axis values do not match the actual values. "
                "Check that you pass correct y-column to the plotting function."
            ),
        )

    def checkCollectionTransparency(self, ax: plt.Axes, expected_alpha: float, collection_number: int = 0):
        actual_alpha = ax.collections[collection_number].get_alpha()
        if actual_alpha is None:
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = "The collection must not be transparent."
        else:
            error_message = f"The collection must have transparency = {expected_alpha} (actual: {actual_alpha})"

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkCollectionColor(self, ax: plt.Axes, expected_facecolor: str, collection_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_facecolor), to_rgb(ax.collections[collection_number].get_facecolor())),
            msg=f"The collection must be colored in '{expected_facecolor}'.",
        )

    def checkNumberOfLines(self, ax: plt.Axes, expected_number: int):
        lines = getattr(ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            f"The figure must have only {expected_number} lines.",
        )

    def checkLinePosition(self, ax: plt.Axes, expected_x: List[float], expected_y: List[float], line_number: int = 0):
        actual_x, actual_y = ax.lines[line_number].get_xydata().T

        self.assertAlmostAllEqual(
            expected_x,
            actual_x,
            msg=(
                "The expected x-axis values do not match the actual values. "
                "Check that you pass correct x-column to the plotting function."
            ),
        )

        self.assertAlmostAllEqual(
            expected_y,
            actual_y,
            msg=(
                "The expected y-axis values do not match the actual values. "
                "Check that you pass correct y-column to the plotting function."
            ),
        )

    def checkLineTransparency(self, ax: plt.Axes, expected_alpha: float, line_number: int = 0):
        actual_alpha = ax.lines[line_number].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = "The line must not be transparent."
        else:
            error_message = f"The line must have transparency = {expected_alpha} (actual: {actual_alpha})."

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkLineColor(self, ax: plt.Axes, expected_color: str, line_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_color), to_rgb(ax.lines[line_number].get_color())),
            msg=f"The line must be colored in '{expected_color}'.",
        )

    def checkLim(self, ax: plt.Axes, expected_lim: List[float], axis: Literal["x", "y"]):
        if axis == "x":
            actual_lim = ax.get_xlim()
        elif axis == "y":
            actual_lim = ax.get_ylim()
        else:
            raise ValueError("Unknown axis name.")

        self.assertAlmostAllEqual(
            expected_lim,
            actual_lim,
            msg=f"The figure should be limited from {expected_lim[0]} to {expected_lim[1]} for {axis}-axis.",
        )

    def checkTitle(self, ax: plt.Axes, expected_title: Optional[str]):
        actual_title = ax.get_title()

        if expected_title is None:
            self.assertEqual("", actual_title, "The figure should have no title")
            return

        self.assertEqual(
            expected_title,
            actual_title,
            f"The figure should be titled as '{expected_title}'",
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
            expected_label,
            actual_label,
            f"The {axis}-axis should be labeled as '{expected_label}'",
        )

    def checkTicks(self, ax: plt.Axes, expected_ticks: List[float], axis: Literal["x", "y"], *, minor: bool = False):
        if axis == "x":
            actual_ticks = ax.get_xticks(minor=minor)
        elif axis == "y":
            actual_ticks = ax.get_yticks(minor=minor)
        else:
            raise ValueError("Unknown axis name.")

        self.assertAlmostAllEqual(
            expected_ticks,
            actual_ticks,
            msg=(
                f"The expected {axis}-axis tick values do not match the actual values. "
                f"Check that you pass the correct values to the `set_{axis}ticks` function."
            ),
        )

    def checkTickLabels(
        self,
        ax: plt.Axes,
        expected_tick_labels: List[str],
        axis: Literal["x", "y"],
        *,
        minor: bool = False,
    ):
        if axis == "x":
            actual_tick_labels = ax.get_xticklabels(minor=minor)
        elif axis == "y":
            actual_tick_labels = ax.get_yticklabels(minor=minor)
        else:
            raise ValueError("Unknown axis name.")

        actual_tick_labels = [label.get_text() for label in actual_tick_labels]

        self.assertListEqual(
            expected_tick_labels,
            actual_tick_labels,
            msg=f"The expected {axis}-axis tick values do not match the actual values.",
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

        self.assertEqual(expected_visibility, actual_visibility, msg=error_message)

    def checkNumberOfContainers(self, ax: plt.Axes, expected_number: int):
        containers = getattr(ax, "containers", [])
        self.assertEqual(
            expected_number,
            len(containers),
            f"The figure must have only {expected_number} containers.",
        )

    def checkContainerType(self, ax: plt.Axes, expected_type: Type[Container], *, container_number: int = 0):
        container = ax.containers[container_number]
        self.assertIsInstance(container, expected_type, f"The container must be {expected_type}.")

    def checkNumberOfPatches(self, ax: plt.Axes, expected_number: int):
        patches = getattr(ax, "patches", [])
        self.assertEqual(
            expected_number,
            len(patches),
            f"The figure must have only {expected_number} patches.",
        )

    def checkPatchesType(self, ax: plt.Axes, expected_type: Type[Patch], *, patch_number: int = 0):
        patch = ax.patches[patch_number]
        self.assertIsInstance(patch, expected_type, f"The patches must be {expected_type}.")

    def checkNumberOfBars(self, ax: plt.Axes, expected_number: int, container_number: int = 0):
        datavalues = ax.containers[container_number].datavalues

        self.assertEqual(
            expected_number,
            len(datavalues),
            f"The figure must have only {expected_number} bars.",
        )

    def checkBarsPosition(self, ax: plt.Axes, expected_position: List[float], *, container_number: int = 0):
        actual_position = ax.containers[container_number].datavalues

        self.assertAlmostAllEqual(
            expected_position,
            actual_position,
            msg="The expected x-axis values do not match the actual values.",
        )

    def checkBarsLayout(
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
            f"The bars must be oriented in the {expected_layout} direction.",
        )

    def checkBarsColor(self, ax: plt.Axes, *, expected_facecolors: List[str], container_number: int = 0):
        actual_colors = [bar.get_facecolor() for bar in ax.containers[container_number]]

        self.assertTrue(
            all(same_color(actual, expected) for actual, expected in zip(actual_colors, expected_facecolors)),
            msg=f"The bars must be colored in '{expected_facecolors}'.",
        )

    def checkPiePosition(self, ax: plt.Axes, expected_position: List[float]):
        expected_patches, _ = ax.pie(expected_position)
        actual_patches = ax.patches

        for actual_wedge, expected_wedge in zip(actual_patches, expected_patches):
            self.assertTrue(
                actual_wedge.center == expected_wedge.center
                and actual_wedge.r == expected_wedge.r
                and actual_wedge.theta1 == expected_wedge.theta1
                and actual_wedge.theta2 == expected_wedge.theta2
                and actual_wedge.width == expected_wedge.width,
                ""  # TODO
            )

    def checkPieLabels(self, ax: plt.Axes, expected_labels: List[str]):
        for actual_patch, expected_label in zip(ax.patches, expected_labels):
            self.assertEqual(
                expected_label,
                actual_patch.get_label(),
                f"The pie labels must be '{expected_label}'.",
            )
