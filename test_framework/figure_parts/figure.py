from typing import List, Union

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


class FigureTestMixin(BaseTestMixin):
    def checkFigureSize(self, ax: plt.Axes, *, expected_width: float, expected_height: float):
        actual_width, actual_height = ax.get_figure().get_size_inches()

        self.assertAllClose(
            [expected_width, expected_height],
            [actual_width, actual_height],
            msg="The expected figure size does not match the actual size.",
        )

    def checkHeightRatio(self, ax: plt.Axes, *, expected_ratio: Union[List[float], List[int]]):
        actual_height_ratio = ax.get_gridspec().get_height_ratios()
        self.assertAllClose(
            expected_ratio,
            actual_height_ratio,
            msg="The expected height ratio does not match the actual one.",
        )
