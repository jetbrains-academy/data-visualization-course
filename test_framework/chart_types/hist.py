from typing import List

import matplotlib.pyplot as plt

from test_framework.chart_types import BarTestMixin


class HistTestMixin(BarTestMixin):
    def checkBarHeights(self, ax: plt.Axes, *, expected_values: List[float], container_number: int = 0):
        actual_heights = [bar.get_height() for bar in ax.containers[container_number]]

        self.assertAllClose(
            expected_values,
            actual_heights,
            msg="The expected bar heights do not match the actual heights.",
        )
