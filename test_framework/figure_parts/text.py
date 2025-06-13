from typing import Literal

import matplotlib.pyplot as plt

from test_framework.base import BaseTestMixin, ColorName


class TextTestMixin(BaseTestMixin):
    def checkNumberOfTextObjects(self, ax: plt.Axes, *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(ax.texts),
            f"The number of text objects must be <samp>{expected_number}</samp>.",
        )

    def checkTextObjects(self, ax: plt.Axes, *, expected_texts: list[tuple[float, float, str]]):
        actual_texts = sorted((*text.get_position(), text.get_text()) for text in ax.texts)
        expected_texts = sorted(expected_texts)

        self.assertAllEqual(expected_texts, actual_texts, "The expected text objects do not match the actual ones.")

    def checkTextObjectHorizontalAlignment(
        self,
        ax: plt.Axes,
        *,
        expected_alignment: Literal["left", "center", "right"],
        text_number: int = 0,
    ):
        actual_alignment = ax.texts[text_number].get_horizontalalignment()

        self.assertEqual(
            expected_alignment,
            actual_alignment,
            msg=(
                f"The text must be aligned to the <samp>{expected_alignment}</samp>, "
                f"but got <samp>{actual_alignment}</samp>."
            ),
        )

    def checkTextObjectColor(self, ax: plt.Axes, *, expected_color: ColorName, text_number: int = 0):
        actual_color = ax.texts[text_number].get_color()

        self.assertSingleColor(
            expected_color,
            actual_color,
            f"The text must have color <samp>{expected_color}</samp>, but got <samp>{actual_color}</samp>.",
        )
