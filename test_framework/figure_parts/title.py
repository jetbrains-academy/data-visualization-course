from typing import Optional

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


class TitleTestMixin(BaseTestMixin):
    def checkTitle(self, ax: plt.Axes, *, expected_title: Optional[str]):
        actual_title = ax.get_title()

        if expected_title is None:
            self.assertTrue(
                actual_title == "",
                msg=f"The axes should have no title, but got <samp>{actual_title}</samp> instead.",
            )
            return

        self.assertEqual(
            expected_title,
            actual_title,
            f"The axes should be titled as <samp>{expected_title}</samp>.",
        )

    def checkSupTitle(self, fig: plt.Figure, *, expected_suptitle: str):
        actual_suptitle = fig.get_suptitle()

        if expected_suptitle is None:
            self.assertTrue(
                actual_suptitle == "",
                msg=f"The figure should have no title, but got <samp>{actual_suptitle}</samp> instead.",
            )
            return

        self.assertEqual(
            expected_suptitle,
            actual_suptitle,
            f"The figure should be titled as <samp>{expected_suptitle}</samp>.",
        )
