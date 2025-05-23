from typing import Optional, Union

from matplotlib.colors import to_rgb
from matplotlib.legend import Legend
import matplotlib.pyplot as plt
import seaborn as sns

from test_framework.base import BaseTestMixin, ColorName


class LegendTestMixin(BaseTestMixin):
    @staticmethod
    def __get_legend(obj: Union[plt.Axes, sns.FacetGrid]) -> Legend:
        if isinstance(obj, plt.Axes):
            return obj.get_legend()

        if isinstance(obj, sns.FacetGrid):
            return obj.legend

        raise TypeError("Unknown object type.")

    # It seems that in seaborn,
    # the legend always exists and also has a visibility property set to "true" for some reason.
    # So this function only works with matplotlib.
    # But anyway this function is just additional to the "main" functions bellow.
    def checkLegendExists(self, ax: plt.Axes):
        self.assertIsNotNone(ax.get_legend(), "Legend must exist.")

    def checkNumberOfLegendItems(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_number: int):
        self.assertEqual(
            expected_number,
            len(self.__get_legend(obj).texts),
            f"The number of legend items must be <samp>{expected_number}</samp>.",
        )

    def checkLegendLabels(self, obj: Union[plt.Axes, sns.FacetGrid], *, expected_labels: list[str]):
        actual_labels = [label.get_text() for label in self.__get_legend(obj).texts]
        self.assertAllEqual(
            expected_labels,
            actual_labels,
            msg="The actual legend labels do not match the expected ones.",
        )

    def checkLegendHandleColors(
        self,
        obj: Union[plt.Axes, sns.FacetGrid],
        *,
        expected_handle_colors: Optional[list[ColorName]],
    ):
        actual_handle_colors = [to_rgb(handle.get_facecolor()) for handle in self.__get_legend(obj).legend_handles]

        self.assertColorList(
            expected_handle_colors,
            actual_handle_colors,
            msg="The expected legend colors do not match the actual ones.",
        )
