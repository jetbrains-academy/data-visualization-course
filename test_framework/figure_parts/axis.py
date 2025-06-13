from typing import Literal, Optional

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


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

    def checkTicks(self, ax: plt.Axes, *, expected_ticks: list[float], axis: Literal["x", "y"], minor: bool = False):
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
        expected_tick_labels: list[str],
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

    def checkLim(self, ax: plt.Axes, *, expected_lim: tuple[float, float], axis: Literal["x", "y"]):
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

    def checkAxisScale(self, ax: plt.Axes, *, expected_scale: Literal["log", "linear"], axis: Literal["x", "y"]):
        if axis == "x":
            actual_scale = ax.get_xscale()
        elif axis == "y":
            actual_scale = ax.get_yscale()
        else:
            raise ValueError("Unknown axis name.")

        self.assertEqual(
            expected_scale,
            actual_scale,
            msg=f"The {axis}-axis scale should be <samp>{expected_scale}</samp>.",
        )
