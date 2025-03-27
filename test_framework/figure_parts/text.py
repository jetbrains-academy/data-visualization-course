from typing import List, Tuple

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin


class TextTestMixin(BaseTestMixin):
    def checkNumberOfTextObjects(self, ax: plt.Axes, *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(ax.texts),
            f"The number of text objects must be <samp>{expected_number}</samp>.",
        )

    def checkTextObjects(self, ax: plt.Axes, *, expected_texts: List[Tuple[float, float, str]]):
        actual_texts = sorted((*text.get_position(), text.get_text()) for text in ax.texts)
        expected_texts = sorted(expected_texts)

        self.assertAllEqual(expected_texts, actual_texts, "The expected text objects do not match the actual ones.")
