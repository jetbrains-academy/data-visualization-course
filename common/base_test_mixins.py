from typing import Any, List, Literal, Optional, Tuple, Type
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

    def checkLegendExists(self, ax: plt.Axes):
        self.assertIsNotNone(ax.get_legend(), "Legend must exist.")

    def checkNumberOfLegendItems(self, ax: plt.Axes, *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(ax.get_legend().texts),
            f"The number of legend items must be {expected_number}.",
        )

    def checkLegendLabels(self, ax: plt.Axes, *, expected_labels: List[str]):
        actual_labels = [label.get_text() for label in ax.get_legend().texts]
        self.assertListEqual(
            expected_labels,
            actual_labels,
            msg=f"The legend labels must be equal to {expected_labels}.",
        )

    def checkLegendHandleColors(self, ax: plt.Axes, *, expected_handle_colors: List[str]):
        actual_handle_colors = [handle.get_facecolor() for handle in ax.get_legend().legend_handles]
        for actual_color, expected_color in zip(actual_handle_colors, expected_handle_colors):
            self.assertTrue(same_color(actual_color, expected_color), msg="The legend handle colors do not match.")

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
        where: Literal["primary", "secondary"] = "primary",
    ):
        if axis == "x":
            axis_obj = ax.xaxis
        elif axis == "y":
            axis_obj = ax.yaxis
        else:
            raise ValueError("Unknown axis name.")

        # As far as I understand, ticks are lazy, so you need to create them to be able to get them.
        # To do it, we have to call this private function.
        # I know it's a bad thing to do, but I believe it is the optional solution.
        axis_obj._update_ticks()  # noqa: SLF001

        ticks = axis_obj.get_minor_ticks() if minor else axis_obj.get_major_ticks()

        if where == "primary":
            actual_tick_labels = [tick.label1.get_text() for tick in ticks if tick.label1.get_visible()]
        elif where == "secondary":
            actual_tick_labels = [tick.label2.get_text() for tick in ticks if tick.label2.get_visible()]
        else:
            raise ValueError("Unknown tick position.")

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

    def checkBarValues(self, ax: plt.Axes, expected_values: List[float], *, container_number: int = 0):
        actual_position = ax.containers[container_number].datavalues

        self.assertAlmostAllEqual(
            expected_values,
            actual_position,
            msg="The expected values do not match the actual values.",
        )

    def checkBarWidth(self, ax: plt.Axes, expected_width: float, *, container_number: int = 0):
        actual_widths = [bar.get_width() for bar in ax.containers[container_number]]
        expected_widths = [expected_width] * len(actual_widths)

        self.assertAlmostAllEqual(
            expected_widths,
            actual_widths,
            msg=f"The bar width should be equal to {expected_width}.",
        )

    def checkBarPositions(
        self,
        ax: plt.Axes,
        expected_positions: List[float],
        *,
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

        self.assertAlmostAllEqual(
            expected_positions,
            actual_positions,
            msg=f"The bar#{container_number} positions should be equal to {expected_positions}.",
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
            f"The bars must be oriented in the {expected_layout} direction.",
        )

    def checkBarColor(self, ax: plt.Axes, *, expected_facecolors: List[str], container_number: int = 0):
        actual_colors = [bar.get_facecolor() for bar in ax.containers[container_number]]

        self.assertTrue(
            all(same_color(actual, expected) for actual, expected in zip(actual_colors, expected_facecolors)),
            msg=f"The bars must be colored in '{expected_facecolors}'.",
        )

    def checkPiePosition(self, ax: plt.Axes, *, expected_position: List[float]):
        expected_patches, _ = ax.pie(expected_position)
        actual_patches = ax.patches

        for actual_wedge, expected_wedge in zip(actual_patches, expected_patches):
            self.assertTrue(
                actual_wedge.r == expected_wedge.r
                and actual_wedge.theta1 == expected_wedge.theta1
                and actual_wedge.theta2 == expected_wedge.theta2,
                "The expected bar values do not match the actual values.",
            )

    def checkPieExplode(
        self,
        ax: plt.Axes,
        *,
        expected_position: List[float],
        expected_explode: Optional[List[float]] = None,
    ):
        expected_patches, _ = ax.pie(expected_position, explode=expected_explode)
        actual_patches = ax.patches

        for actual_wedge, expected_wedge in zip(actual_patches, expected_patches):
            self.assertTrue(
                expected_wedge.center == actual_wedge.center,
                "The expected explode values do not match the actual values.",
            )

    def checkPieLabels(self, ax: plt.Axes, expected_labels: List[str]):
        for actual_patch, expected_label in zip(ax.patches, expected_labels):
            self.assertEqual(
                expected_label,
                actual_patch.get_label(),
                f"The pie label must be '{expected_label}'.",
            )

    def checkPieColors(self, ax: plt.Axes, expected_colors: List[str]):
        for actual_patch, expected_color in zip(ax.patches, expected_colors):
            self.assertTrue(
                same_color(actual_patch.get_facecolor(), expected_color),
                f"The wedges must be colored in '{expected_colors}'.",
            )

    def checkPieNumericLabels(self, ax: plt.Axes, expected_labels: List[str]):
        for actual_label, expected_label in zip(ax.texts[1::2], expected_labels):
            self.assertEqual(
                expected_label,
                actual_label.get_text(),
                f"The numeric label must be '{expected_label}'.",
            )

    def checkNumberOfTextObjects(self, ax: plt.Axes, expected_number: int):
        self.assertEqual(expected_number, len(ax.texts), f"The number of text objects must be {expected_number}.")

    def checkTextObjects(self, ax: plt.Axes, expected_texts: List[Tuple[float, float, str]]):
        actual_texts = sorted((*text.get_position(), text.get_text()) for text in ax.texts)
        expected_texts = sorted(expected_texts)

        self.assertListEqual(expected_texts, actual_texts, "")
