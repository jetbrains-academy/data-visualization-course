from typing import List

import matplotlib.pyplot as plt

from test_framework.chart_types import BarTestMixin


class HistTestMixin(BarTestMixin):
    def checkBarHeights(self, ax: plt.Axes, *, expected_values: List[float], container_number: int = 0):
        actual_heights = [bar.get_height() for bar in ax.containers[container_number]]

        self.assertAllClose(
            expected_values,
            actual_heights,
            msg=f"The expected bar heights in container#{container_number} do not match the actual heights.",
        )

    def checkBarBins(self, ax: plt.Axes, *, expected_bins: List[float], container_number: int = 0):
        actual_bins = [bar.get_x() for bar in ax.containers[container_number]]

        # Add the last bin edge
        actual_bins.append(actual_bins[-1] + ax.containers[container_number][-1].get_width())

        self.assertAllClose(
            expected_bins,
            actual_bins,
            msg=f"The expected bar bins in container#{container_number} do not match the actual bins.",
        )

    def checkBarTransparency(self, ax: plt.Axes, *, expected_alpha: float, container_number: int = 0):
        actual_alpha = ax.containers[container_number][0].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = (
                f"The bars in container#{container_number} must not be transparent, but got "
                f"<samp>{actual_alpha}</samp>."
            )
        else:
            error_message = (
                f"The bars in container#{container_number} must have transparency equal to "
                f"<samp>{expected_alpha}</samp>, but got <samp>{actual_alpha}</samp>."
            )

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkStepHistBins(self, ax: plt.Axes, *, expected_bins: List[float], patch_number: int = 0):
        actual_bins = ax.patches[patch_number].get_path().vertices[:, 0][::2].tolist()

        self.assertAllClose(
            expected_bins,
            actual_bins,
            msg=f"The expected step hist bins in patch#{patch_number} do not match the actual bins.",
        )

    def checkStepHistHeights(self, ax: plt.Axes, *, expected_values: List[float], patch_number: int = 0):
        actual_heights = ax.patches[patch_number].get_path().vertices[:, 1][::2].tolist()[1:]

        self.assertAllClose(
            expected_values,
            actual_heights,
            msg=f"The expected step hist heights in patch#{patch_number} do not match the actual heights.",
        )

    def checkStepHistTransparency(self, ax: plt.Axes, *, expected_alpha: float, patch_number: int = 0):
        actual_alpha = ax.patches[patch_number].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = (
                f"The step hist in patch#{patch_number} must not be transparent, but got <samp>{actual_alpha}</samp>."
            )
        else:
            error_message = (
                f"The step hist in patch#{patch_number} must have transparency equal to <samp>{expected_alpha}</samp>, "
                f"but got <samp>{actual_alpha}</samp>."
            )

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)
