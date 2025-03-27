from typing import Optional

from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin, ColorName


class CollectionTestMixin(BaseTestMixin):
    def checkCollectionPosition(
        self,
        ax: plt.Axes,
        *,
        expected_x: list[float],
        expected_y: list[float],
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

    def checkCollectionTransparency(self, ax: plt.Axes, *, expected_alpha: float, collection_number: int = 0):
        actual_alpha = ax.collections[collection_number].get_alpha()
        if actual_alpha is None:
            # If alpha is None, then it by default equals 1
            actual_alpha = 1

        if expected_alpha == 1:
            error_message = f"The collection must not be transparent, but got <samp>{actual_alpha}</samp>."
        else:
            error_message = (
                f"The collection must have transparency equal to <samp>{expected_alpha}</samp>, "
                f"but got <samp>{actual_alpha}</samp>."
            )

        self.assertAlmostEqual(expected_alpha, actual_alpha, msg=error_message)

    def checkCollectionColor(
        self,
        ax: plt.Axes,
        *,
        expected_facecolor: Optional[ColorName],
        collection_number: int = 0,
    ):
        actual_color = to_rgb(ax.collections[collection_number].get_facecolor())

        self.assertSingleColor(
            expected_facecolor,
            actual_color,
            msg=(
                f"The collection must be colored in <samp>{expected_facecolor}</samp>, "
                f"but got <samp>{self._rgb_to_name(actual_color)}</samp>."
            ),
        )
