from typing import List, Literal, Optional, Tuple, Union

from matplotlib.colors import to_rgb
from matplotlib.legend import Legend
import matplotlib.pyplot as plt
import seaborn as sns

from test_framework.base import BaseTestMixin, ColorName

__all__ = ["TitleTestMixin", "AxisTestMixin", "LegendTestMixin", "SpineTestMixin", "TextTestMixin"]


class TitleTestMixin(BaseTestMixin):
    def checkTitle(self, ax: plt.Axes, *, expected_title: Optional[str]):
        actual_title = ax.get_title()

        if expected_title is None:
            self.assertTrue(
                actual_title == "",
                msg=f"The figure should have no title, but got <samp>{actual_title}</samp> instead.",
            )
            return

        self.assertEqual(
            expected_title,
            actual_title,
            f"The figure should be titled as <samp>{expected_title}</samp>.",
        )


class AxisTestMixin(BaseTestMixin):
    def checkLabel(self, ax: plt.Axes, *, expected_label: Optional[str], axis: Literal["x", "y"]):
        if axis == "x":
            actual_label = ax.get_xlabel()
        elif axis == "y":
            actual_label = ax.get_ylabel()
        else:
            raise ValueError("Unknown axis name.")

        if expected_label is None:
            self.assertTrue(
                actual_label == "",
                msg=f"The {axis}-axis should have no label, but got <samp>{actual_label}</samp> instead.",
            )
            return

        self.assertEqual(
            expected_label,
            actual_label,
            f"The {axis}-axis should be labeled as <samp>{expected_label}</samp>.",
        )

    def checkTicks(self, ax: plt.Axes, *, expected_ticks: List[float], axis: Literal["x", "y"], minor: bool = False):
        if axis == "x":
            actual_ticks = ax.get_xticks(minor=minor)
        elif axis == "y":
            actual_ticks = ax.get_yticks(minor=minor)
        else:
            raise ValueError("Unknown axis name.")

        self.assertAllClose(
            expected_ticks,
            actual_ticks,
            msg=f"The expected {axis}-axis tick values do not match the actual values.",
        )

    def checkTickLabels(
        self,
        ax: plt.Axes,
        *,
        expected_tick_labels: List[str],
        axis: Literal["x", "y"],
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

    def checkLim(self, ax: plt.Axes, *, expected_lim: Tuple[float, float], axis: Literal["x", "y"]):
        if axis == "x":
            actual_lim = ax.get_xlim()
        elif axis == "y":
            actual_lim = ax.get_ylim()
        else:
            raise ValueError("Unknown axis name.")

        expected_left_bound, expected_right_bound = expected_lim
        actual_left_bound, actual_right_bound = actual_lim

        msg = (
            f"The figure should be limited from <samp>{expected_left_bound}</samp> to "
            f"<samp>{expected_right_bound}</samp> for {axis}-axis, "
            f"but limited from <samp>{actual_left_bound}</samp> to <samp>{actual_right_bound}</samp> instead."
        )

        self.assertAlmostEqual(
            expected_left_bound,
            actual_left_bound,
            msg=msg,
        )

        self.assertAlmostEqual(
            expected_right_bound,
            actual_right_bound,
            msg=msg,
        )


class LegendTestMixin(BaseTestMixin):
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
            f"The number of legend items must be <samp>{expected_number}</samp>.",
        )

    def checkLegendLabels(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_labels: List[str]):
        actual_labels = [label.get_text() for label in self.__get_legend(obj).texts]
        self.assertAllEqual(
            expected_labels,
            actual_labels,
            msg="The actual legend labels do not match the expected ones.",
        )

    def checkLegendHandleColors(
        self,
        obj: Union[plt.Axes, sns.FacetGrid],
        *,
        expected_handle_colors: Optional[List[ColorName]],
    ):
        actual_handle_colors = [to_rgb(handle.get_facecolor()) for handle in self.__get_legend(obj).legend_handles]

        self.assertColorList(
            expected_handle_colors,
            actual_handle_colors,
            msg="The expected legend colors do not match the actual ones.",
        )


class SpineTestMixin(BaseTestMixin):
    def checkSpineVisibility(
        self,
        ax: plt.Axes,
        *,
        position: Literal["left", "right", "top", "bottom"],
        expected_visibility: bool,
    ):
        actual_visibility = ax.spines[position].get_visible()

        if expected_visibility:
            error_message = f"The {position} spine must be visible."
        else:
            error_message = f"The {position} spine must not be visible."

        self.assertTrue(expected_visibility == actual_visibility, msg=error_message)


class TextTestMixin(BaseTestMixin):
    def checkNumberOfTextObjects(self, ax: plt.Axes, *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(ax.texts),
            f"The number of text objects must be <samp>{expected_number}</samp>.",
        )

    def checkTextObjects(self, ax: plt.Axes, *, expected_texts: List[Tuple[float, float, str]]):
        actual_texts = sorted((*text.get_position(), text.get_text()) for text in ax.texts)
        expected_texts = sorted(expected_texts)

        self.assertAllEqual(expected_texts, actual_texts, "The expected text objects do not match the actual ones.")
