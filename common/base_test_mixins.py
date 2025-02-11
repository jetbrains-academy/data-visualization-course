from typing import Any, ClassVar, List, Literal, Optional, Tuple, Type, Union
from unittest import TestCase

import matplotlib.colors as mcolors
from matplotlib.colors import same_color, to_rgb
from matplotlib.container import Container
from matplotlib.legend import Legend
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose
import seaborn as sns

colors_to_avoid = ["aqua", "darkgray", "darkslategray", "dimgray", "fuchsia", "gray", "lightgray",
                   "lightslategray",
                   "slategray"]


class BaseTestMixin(TestCase):
    longMessage = False
    named_colors: ClassVar[dict] = {name: mcolors.to_rgb(name) for name in mcolors.CSS4_COLORS if
                                    name not in colors_to_avoid}

    # Add tab10 colors for checking default colors assigned to plots
    tab10_colors: ClassVar[dict] = {f"C{i}": to_rgb(name) for i, name in enumerate(mcolors.TABLEAU_COLORS)}
    named_colors.update(tab10_colors)

    def rgb_to_names(self, color: tuple) -> Union[str, tuple]:
        return next((name for name, value in self.named_colors.items() if value == color), color)

    def assertAllClose(self, expected: list, actual: list, msg: str):
        # The numpy error message is not compatible with the plugin,
        # so we reraise it via unittest appending a custom message
        try:
            assert_allclose(actual, expected)
        except AssertionError as e:
            raise self.failureException(msg + str(e)) from None

    def assertAllEqual(self, expected: list, actual: list, msg: str):
        try:
            self.assertListEqual(expected, actual)
        except AssertionError as e:
            error_string = f"{msg}\n\nExpected: {expected}\nActual: {actual}\n\n{e!s}"
            raise self.failureException(error_string) from None

    @staticmethod
    def addExpectedAndActualToMessage(expected: Any, actual: Any, msg: str) -> str:
        return f"{msg}\n\nExpected: {expected}\nActual: {actual}"

    def assertColorList(self, expected_colors: List[str], actual_colors: List[tuple], msg: str):
        actual_colors_names = [self.rgb_to_names(color) for color in actual_colors]
        expected_colors_rgb = [to_rgb(color) for color in expected_colors]

        self.assertListEqual(
            expected_colors_rgb,
            actual_colors,
            self.addExpectedAndActualToMessage(expected_colors, actual_colors_names, msg),
        )

    def assertSingleColor(self, expected_color: str, actual_color: tuple, msg: str):
        self.assertTrue(
            same_color(to_rgb(expected_color), actual_color),
            msg=msg,
        )

    # ----------------------------------------------------------------------

    def checkReturnType(self, obj: Any, expected_type: Any, expected_function: Optional[str] = None):
        string_expected_type = expected_type.__name__
        error_message = f"The return type is wrong. You should return {string_expected_type}, but got {type(obj)}."

        if expected_function is not None:
            if "plt" in expected_function:
                error_message += f" Please return the figure from `plt.subplots`"
            else:
                error_message += f" Please use `{expected_function}`."

        self.assertIsInstance(
            obj,
            expected_type,
            error_message,
        )

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
    def __get_legend(obj: Union[plt.Axes, sns.FacetGrid]) -> Legend:
        if isinstance(obj, plt.Axes):
            return obj.get_legend()

        if isinstance(obj, sns.FacetGrid):
            return obj.legend

        raise TypeError("Unknown object type.")

    # It seems that in seaborn,
    # the legend always exists and also has a visibility property set to "true" for some reason.
    # So this function only works with matplotlib.
    # But anyway this function is just additional to the "main" functions bellow.
    def checkLegendExists(self, ax: plt.Axes):
        self.assertIsNotNone(ax.get_legend(), "Legend must exist.")

    def checkNumberOfLegendItems(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(self.__get_legend(obj).texts),
            f"The number of legend items must be {expected_number}.",
        )

    def checkLegendLabels(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_labels: List[str]):
        actual_labels = [label.get_text() for label in self.__get_legend(obj).texts]
        self.assertAllEqual(
            expected_labels,
            actual_labels,
            msg=f"The legend labels must be equal to {expected_labels}.",
        )

    def checkLegendHandleColors(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_handle_colors: List[str]):
        actual_handle_colors = [to_rgb(handle.get_facecolor()) for handle in self.__get_legend(obj).legend_handles]
        self.assertColorList(expected_handle_colors, actual_handle_colors, "The legend colors do not match.")

    def checkCollectionPosition(
            self,
            ax: plt.Axes,
            expected_x: List[float],
            expected_y: List[float],
            collection_number: int = 0,
    ):
        actual_x, actual_y = ax.collections[collection_number].get_offsets().T

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

    def checkCollectionTransparency(self, ax: plt.Axes, expected_alpha: float, collection_number: int = 0):
        actual_alpha = ax.collections[collection_number].get_alpha()
        if actual_alpha is None:
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = "The collection must not be transparent."
        else:
            error_message = f"The collection must have transparency = {expected_alpha}, but got {actual_alpha}."

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkCollectionColor(self, ax: plt.Axes, expected_facecolor: str, collection_number: int = 0):
        actual_color = to_rgb(ax.collections[collection_number].get_facecolor())
        self.assertSingleColor(expected_facecolor, actual_color,
                               f"The collection must be colored in '{expected_facecolor}', but got '{self.rgb_to_names(actual_color)}'.")

    def checkNumberOfLines(self, ax: plt.Axes, expected_number: int):
        lines = getattr(ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            f"The figure must have only {expected_number} lines.",
        )

    def checkLinePosition(self, ax: plt.Axes, expected_x: List[float], expected_y: List[float], line_number: int = 0):
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

    def checkLineTransparency(self, ax: plt.Axes, expected_alpha: float, line_number: int = 0):
        actual_alpha = ax.lines[line_number].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = "The line must not be transparent."
        else:
            error_message = f"The line must have transparency = {expected_alpha}, but got {actual_alpha}."

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkLineColor(self, ax: plt.Axes, expected_color: str, line_number: int = 0):
        actual_color = to_rgb(ax.lines[line_number].get_color())
        self.assertSingleColor(expected_color, actual_color,
                               f"The line must be colored in '{expected_color}', but got '{self.rgb_to_names(actual_color)}'.")

    def checkLim(self, ax: plt.Axes, expected_lim: List[float], axis: Literal["x", "y"]):
        if axis == "x":
            actual_lim = ax.get_xlim()
        elif axis == "y":
            actual_lim = ax.get_ylim()
        else:
            raise ValueError("Unknown axis name.")

        self.assertAllClose(
            expected_lim,
            actual_lim,
            msg=f"The figure should be limited from {expected_lim[0]} to {expected_lim[1]} for {axis}-axis.",
        )

    def checkTitle(self, ax: plt.Axes, expected_title: Optional[str]):
        actual_title = ax.get_title()

        if expected_title is None:
            self.assertEqual("", actual_title, "The figure should have no title.")
            return

        self.assertEqual(
            expected_title,
            actual_title,
            f"The figure should be titled as '{expected_title}'.",
        )

    def checkLabel(self, ax: plt.Axes, expected_label: Optional[str], axis: Literal["x", "y"]):
        if axis == "x":
            actual_label = ax.get_xlabel()
        elif axis == "y":
            actual_label = ax.get_ylabel()
        else:
            raise ValueError("Unknown axis name.")

        if expected_label is None:
            self.assertEqual("", actual_label, f"The {axis}-axis should have no labels.")
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

        self.assertAllClose(
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

        self.assertAllEqual(
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
        string_expected_type = expected_type.__name__
        self.assertIsInstance(
            container,
            expected_type,
            self.addExpectedAndActualToMessage(
                expected_type,
                type(container),
                f"Incorrect chart type. You should plot {string_expected_type}, but got {type(container).__name__}.",
            ),
        )

    def checkNumberOfPatches(self, ax: plt.Axes, expected_number: int):
        patches = getattr(ax, "patches", [])
        self.assertEqual(
            expected_number,
            len(patches),
            f"The figure must have only {expected_number} patches.",
        )

    def checkPatchesType(self, ax: plt.Axes, expected_type: Type[Patch], *, patch_number: int = 0):
        patch = ax.patches[patch_number]
        string_expected_type = expected_type.__name__
        self.assertIsInstance(
            patch,
            expected_type,
            self.addExpectedAndActualToMessage(
                expected_type,
                type(patch),
                f"Incorrect chart type. You should plot {string_expected_type}, but got {type(patch).__name__}.",
            ),
        )

    def checkNumberOfBars(self, ax: plt.Axes, expected_number: int, container_number: int = 0):
        datavalues = ax.containers[container_number].datavalues

        self.assertEqual(
            expected_number,
            len(datavalues),
            f"The figure must have only {expected_number} bars.",
        )

    def checkBarValues(self, ax: plt.Axes, expected_values: List[float], *, container_number: int = 0):
        actual_position = ax.containers[container_number].datavalues

        self.assertAllClose(
            expected_values,
            actual_position,
            msg="The expected bar values do not match the actual values.",
        )

    def checkBarWidth(self, ax: plt.Axes, expected_width: float, *, container_number: int = 0):
        actual_widths = [bar.get_width() for bar in ax.containers[container_number]]
        expected_widths = [expected_width] * len(actual_widths)

        self.assertAllClose(
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

        self.assertAllClose(
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
        actual_colors = [to_rgb(bar.get_facecolor()) for bar in ax.containers[container_number]]
        self.assertColorList(expected_facecolors, actual_colors, "The bar colors do not match.")

    def checkPiePosition(self, ax: plt.Axes, *, expected_position: List[float]):
        fig, ax_test = plt.subplots()
        expected_patches, _ = ax_test.pie(expected_position)
        actual_patches = ax.patches

        for i, (actual_wedge, expected_wedge) in enumerate(zip(actual_patches, expected_patches)):
            label = actual_wedge.get_label()
            if not label:
                label = str(i + 1)
            self.assertAlmostEqual(
                actual_wedge.r,
                expected_wedge.r,
                msg=self.addExpectedAndActualToMessage(
                    expected_wedge.r,
                    actual_wedge.r,
                    f"The expected {label} wedge radius does not match the actual value.",
                ),
            )

            self.assertAlmostEqual(
                actual_wedge.theta1,
                expected_wedge.theta1,
                msg=self.addExpectedAndActualToMessage(
                    expected_wedge.theta1,
                    actual_wedge.theta1,
                    f"The expected {label} wedge start angle does not match the actual value.",
                ),
            )

            self.assertAlmostEqual(
                actual_wedge.theta2,
                expected_wedge.theta2,
                msg=self.addExpectedAndActualToMessage(
                    expected_wedge.theta2,
                    actual_wedge.theta2,
                    f"The expected {label} wedge end angle does not match the actual value.",
                ),
            )

    def checkPieExplode(
            self,
            ax: plt.Axes,
            *,
            expected_position: List[float],
            expected_explode: Optional[List[float]] = None,
    ):
        fig, ax_test = plt.subplots()
        expected_patches, _ = ax_test.pie(expected_position, explode=expected_explode)
        actual_patches = ax.patches

        for i, (actual_patch, expected_patch) in enumerate(zip(actual_patches, expected_patches)):
            label = actual_patch.get_label()
            if not label:
                label = str(i + 1)

            self.assertAlmostEqual(
                expected_patch.center,
                actual_patch.center,
                msg=self.addExpectedAndActualToMessage(
                    expected_patch.center,
                    actual_patch.center,
                    f"The expected {label} wedge explode value does not match the actual value.",
                ),
            )

    def checkPieLabels(self, ax: plt.Axes, expected_labels: List[str]):
        for i, (actual_patch, expected_label) in enumerate(zip(ax.patches, expected_labels)):
            label = actual_patch.get_label()
            if not label:
                label = str(i + 1)

            self.assertEqual(
                expected_label,
                actual_patch.get_label(),
                f"The {label} pie label must be '{expected_label}'.",
            )

    def checkPieColors(self, ax: plt.Axes, expected_colors: List[str]):
        actual_colors = [to_rgb(patch.get_facecolor()) for patch in ax.patches]
        self.assertColorList(expected_colors, actual_colors, "The pie colors do not match.")

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

        self.assertAllEqual(expected_texts, actual_texts, "The text objects do not match.")
