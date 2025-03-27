from typing import Optional

from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin, ColorName


class PieTestMixin(BaseTestMixin):
    def checkPiePosition(self, ax: plt.Axes, *, expected_position: list[float]):
        fig, expected_ax = plt.subplots()
        expected_patches, _ = expected_ax.pie(expected_position)
        actual_patches = ax.patches

        for i, (actual_wedge, expected_wedge) in enumerate(zip(actual_patches, expected_patches)):
            label = actual_wedge.get_label()
            if not label:
                label = str(i + 1)

            msg = (
                f"The expected wedge#{label} position does not match the actual one. "
                f"Please see the full feedback for more information.\n\n"
            )

            self.assertAlmostEqual(
                actual_wedge.r,
                expected_wedge.r,
                msg=(
                    msg + f"The wedge#{label} radius should be equal to <samp>{expected_wedge.r}</samp>, "
                    f"but got <samp>{actual_wedge.r}</samp>."
                ),
            )

            self.assertAlmostEqual(
                actual_wedge.theta1,
                expected_wedge.theta1,
                msg=(
                    msg + f"The wedge#{label} start angle should be equal to <samp>{expected_wedge.theta1}</samp>, "
                    f"but got <samp>{actual_wedge.theta1}</samp>."
                ),
            )

            self.assertAlmostEqual(
                actual_wedge.theta2,
                expected_wedge.theta2,
                msg=(
                    msg + f"The wedge#{label} end angle should be equal to <samp>{expected_wedge.theta2}</samp>, "
                    f"but got <samp>{actual_wedge.theta2}</samp>."
                ),
            )

    def checkPieExplode(
        self,
        ax: plt.Axes,
        *,
        expected_position: list[float],
        expected_explode: Optional[list[float]] = None,
    ):
        fig, expected_ax = plt.subplots()
        expected_patches, _ = expected_ax.pie(expected_position, explode=expected_explode)
        actual_patches = ax.patches

        for i, (actual_patch, expected_patch) in enumerate(zip(actual_patches, expected_patches)):
            label = actual_patch.get_label()
            if not label:
                label = str(i + 1)

            actual_center_x, actual_center_y = actual_patch.center
            expected_center_x, expected_center_y = expected_patch.center

            if expected_explode is None:
                msg = f"The wedge#{label} should not be offset. "
            else:
                msg = f"The expected wedge#{label} offset does not match the actual value. "

            msg += (
                "Please see the full feedback for more information.\n\n"
                f"The expected wedge center should be equal to <samp>{expected_patch.center}</samp>, "
                f"but got <samp>{actual_patch.center}</samp>."
            )

            self.assertAlmostEqual(expected_center_x, actual_center_x, msg=msg)
            self.assertAlmostEqual(expected_center_y, actual_center_y, msg=msg)

    def checkPieLabels(self, ax: plt.Axes, *, expected_labels: list[str]):
        actual_labels = [actual_patch.get_label() for actual_patch in ax.patches]
        self.assertAllEqual(
            expected_labels,
            actual_labels,
            msg="The expected pie labels do not match the actual ones.",
        )

    def checkPieColors(self, ax: plt.Axes, *, expected_colors: Optional[list[ColorName]]):
        actual_colors = [to_rgb(patch.get_facecolor()) for patch in ax.patches]

        self.assertColorList(
            expected_colors,
            actual_colors,
            msg="The expected pie colors do not match the actual ones.",
        )

    def checkPieNumericLabels(self, ax: plt.Axes, *, expected_labels: list[str]):
        actual_labels = [actual_label.get_text() for actual_label in ax.texts[1::2]]
        self.assertAllEqual(
            expected_labels,
            actual_labels,
            msg="The expected numeric pie labels do not match the actual ones.",
        )
