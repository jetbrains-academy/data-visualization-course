from typing import List

import matplotlib.pyplot as plt

from test_framework.chart_types import BarTestMixin


class HistTestMixin(BarTestMixin):
    def checkBarHeights(
        self,
        ax: plt.Axes,
        *,
        expected_values: List[float],
        container_number: int = 0,
        histtype: str = "bar",
    ):
        if histtype == "bar":
            actual_heights = [bar.get_height() for bar in ax.containers[container_number]]
            component = "container"
        elif histtype == "step":
            actual_heights = ax.patches[container_number].get_path().vertices[:, 1][::2].tolist()[1:]
            component = "patch"
        else:
            raise ValueError("Unknown histtype parameter.")

        self.assertAllClose(
            expected_values,
            actual_heights,
            msg=f"The expected bar heights in {component}#{container_number} do not match the actual heights.",
        )

    def checkBarBins(
        self,
        ax: plt.Axes,
        *,
        expected_bins: List[float],
        container_number: int = 0,
        histtype: str = "bar",
    ):
        if histtype == "bar":
            actual_bins = [bar.get_x() for bar in ax.containers[container_number]]
            # Add the last bin edge
            actual_bins.append(actual_bins[-1] + ax.containers[container_number][-1].get_width())
            component = "container"
        elif histtype == "step":
            actual_bins = ax.patches[container_number].get_path().vertices[:, 0][::2].tolist()
            component = "patch"
        else:
            raise ValueError("Unknown histtype parameter.")

        self.assertAllClose(
            expected_bins,
            actual_bins,
            msg=f"The expected bar bins in {component}#{container_number} do not match the actual bins.",
        )

    def checkBarTransparency(
        self,
        ax: plt.Axes,
        *,
        expected_alpha: float,
        container_number: int = 0,
        histtype: str = "bar",
    ):
        if histtype == "bar":
            actual_alpha = ax.containers[container_number][0].get_alpha()
            component = "container"
        elif histtype == "step":
            actual_alpha = ax.patches[container_number].get_alpha()
            component = "patch"
        else:
            raise ValueError("Unknown histtype parameter.")

        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = (
                f"The bars in {component}#{container_number} must not be transparent, but got "
                f"<samp>{actual_alpha}</samp>."
            )
        else:
            error_message = (
                f"The bars in {component}#{container_number} must have transparency equal to "
                f"<samp>{expected_alpha}</samp>, but got <samp>{actual_alpha}</samp>."
            )

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)
