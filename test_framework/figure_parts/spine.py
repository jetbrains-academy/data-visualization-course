from typing import Literal

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


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
