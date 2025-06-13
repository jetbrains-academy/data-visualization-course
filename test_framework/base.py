import itertools
from typing import Any, ClassVar, Optional, Union
from unittest import TestCase

import matplotlib.colors as mcolors
from matplotlib.colors import same_color, to_rgb
from matplotlib.container import Container
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose
import seaborn as sns

ColorName = str
RGBColor = tuple[float, float, float]


class BaseTestMixin(TestCase):
    # We don't want default messages to be included along with our custom ones
    longMessage = False

    __named_colors: ClassVar[dict[ColorName, RGBColor]] = {
        name: mcolors.to_rgb(name)
        for name in mcolors.CSS4_COLORS
        # We prefer to use "grey" instead of "gray",
        # "cyan" instead of "aqua" and "magenta" instead of "fuchsia"
        if "gray" not in name and name not in ("aqua", "fuchsia")
    }

    def _rgb_to_name(self, color: RGBColor) -> Union[ColorName, RGBColor]:
        return next((name for name, value in self.__named_colors.items() if value == color), color)

    def assertAllClose(self, expected: list, actual: list, msg: str):
        # The numpy error message is not compatible with the plugin,
        # so we reraise it via unittest appending a custom message
        try:
            assert_allclose(actual, expected)
        except AssertionError as e:
            msg = f"{msg} Please see the full feedback for more information.\n\n{e!s}"
            raise self.failureException(msg) from None

    def assertAllEqual(self, expected: list, actual: list, msg: str):
        try:
            self.assertListEqual(expected, actual)
        except AssertionError as e:
            error_string = (
                f"{msg} Please see the full feedback for more information.\n\n"
                f"Expected: {expected}\nActual: {actual}\n\n{e!s}"
            )
            raise self.failureException(error_string) from None

    def assertColorList(self, expected_colors: list[ColorName], actual_colors: list[RGBColor], msg: str):
        actual_colors_names = [self._rgb_to_name(color) for color in actual_colors]

        if expected_colors is None:
            self.assertTrue(
                all(
                    actual == expected
                    for actual, expected in zip(
                        actual_colors,
                        itertools.cycle(map(to_rgb, mcolors.TABLEAU_COLORS.values())),
                    )
                ),
                msg="You do not need to change default figure colors.",
            )
            return

        expected_colors_rgb = [to_rgb(color) for color in expected_colors]
        self.assertListEqual(
            expected_colors_rgb,
            actual_colors,
            msg=(
                f"{msg} Please see the full feedback for more information\n\n"
                f"Expected: {expected_colors}\nActual: {actual_colors_names}"
            ),
        )

    def assertSingleColor(self, expected_color: ColorName, actual_color: RGBColor, msg: str):
        if expected_color is None:
            self.assertTrue(
                same_color(to_rgb(next(iter(mcolors.TABLEAU_COLORS.values()))), actual_color),
                msg="You do not need to change the default figure color.",
            )
            return

        self.assertTrue(
            same_color(to_rgb(expected_color), actual_color),
            msg=msg,
        )

    # ----------------------------------------------------------------------

    def checkReturnType(self, obj: Any, *, expected_type: Any, expected_function: Optional[str] = None):
        error_message = (
            f"The return type is wrong: "
            f"you should return <samp>{expected_type.__name__}</samp>, but got <samp>{type(obj).__name__}</samp>."
        )

        if expected_type == plt.Figure:
            if expected_function is not None:
                raise ValueError("Expected function should not be specified for plt.Figure.")

            error_message += " Please return <samp>Figure</samp> obtained from <samp>plt.subplots</samp>."

        elif expected_type == sns.FacetGrid:
            if expected_function is None:
                raise ValueError("Expected function should be specified for sns.FacetGrid.")

            error_message += f" Please return the result of calling <samp>{expected_function}</samp>."

        else:
            raise ValueError("Unknown return type.")

        self.assertIsInstance(
            obj,
            expected_type,
            error_message,
        )

    def checkNumberOfAxes(self, axes: list[plt.Axes], *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(axes),
            f"The figure must have only <samp>{expected_number}</samp> axes.",
        )

    def checkNumberOfCollections(self, ax: plt.Axes, *, expected_number: int):
        collections = getattr(ax, "collections", [])
        self.assertEqual(
            expected_number,
            len(collections),
            f"The figure must have only <samp>{expected_number}</samp> collections.",
        )

    def checkNumberOfLines(self, ax: plt.Axes, *, expected_number: int):
        lines = getattr(ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            f"The figure must have only <samp>{expected_number}</samp> lines.",
        )

    def checkNumberOfContainers(self, ax: plt.Axes, *, expected_number: int):
        containers = getattr(ax, "containers", [])
        self.assertEqual(
            expected_number,
            len(containers),
            f"The figure must have only <samp>{expected_number}</samp> containers.",
        )

    def checkContainerType(self, ax: plt.Axes, *, expected_type: type[Container], container_number: int = 0):
        container = ax.containers[container_number]
        self.assertIsInstance(
            container,
            expected_type,
            msg=(
                f"Incorrect chart type: you should plot <samp>{expected_type.__name__}</samp>, "
                f"but got <samp>{type(container).__name__}</samp>."
            ),
        )

    def checkNumberOfPatches(self, ax: plt.Axes, *, expected_number: int):
        patches = getattr(ax, "patches", [])
        self.assertEqual(
            expected_number,
            len(patches),
            f"The figure must have only <samp>{expected_number}</samp> patches.",
        )

    def checkPatchType(self, ax: plt.Axes, *, expected_type: type[Patch], patch_number: int = 0):
        patch = ax.patches[patch_number]
        self.assertIsInstance(
            patch,
            expected_type,
            msg=(
                f"Incorrect chart type: you should plot <samp>{expected_type.__name__}</samp>, "
                f"but got <samp>{type(patch).__name__}</samp>."
            ),
        )
