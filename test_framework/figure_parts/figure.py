from types import ModuleType
from unittest.mock import patch

import matplotlib.pyplot as plt
import pandas as pd

from test_framework.base import BaseTestMixin


class FigureTestMixin(BaseTestMixin):
    def checkFigureWidth(self, ax: plt.Axes, *, expected_width: float):
        actual_width, _ = ax.get_figure().get_size_inches()
        error_message = (
            f"The expected figure width is <samp>{expected_width}</samp>, but got <samp>{actual_width}</samp>.",
        )

        self.assertAlmostEqual(
            expected_width,
            actual_width,
            msg=error_message,
        )

    def checkFigureHeight(self, ax: plt.Axes, *, expected_height: float):
        _, actual_height = ax.get_figure().get_size_inches()
        error_message = (
            f"The expected figure height is <samp>{expected_height}</samp>, but got <samp>{actual_height}</samp>.",
        )

        self.assertAlmostEqual(
            expected_height,
            actual_height,
            msg=error_message,
        )

    def checkHeightRatio(self, ax: plt.Axes, *, expected_ratio: list[float]):
        actual_height_ratio = ax.get_gridspec().get_height_ratios()
        self.assertAllClose(
            expected_ratio,
            actual_height_ratio,
            msg="The expected height ratio does not match the actual one.",
        )

    @staticmethod
    def checkTightLayout(*, plot_module: ModuleType, data: pd.DataFrame):
        with patch.object(plot_module.plt.Figure, "tight_layout") as mock_tl:
            plot_module.plot(data)
            mock_tl.assert_called_once()
