from typing import Optional

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


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
