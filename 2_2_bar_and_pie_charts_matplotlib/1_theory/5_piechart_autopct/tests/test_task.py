from typing import ClassVar

from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import pandas as pd

from common.base_test_mixins import BaseTestMixin
from data import aggregate, filter_platforms, preprocess, read
from task import plot


class PlotTestCase(BaseTestMixin):
    data: ClassVar[pd.DataFrame]
    fig: ClassVar[plt.Figure]

    aggregated_data: ClassVar[pd.DataFrame]

    @classmethod
    def setUpClass(cls):
        data = read()
        data = preprocess(data)

        cls.data = data
        cls.fig = plot(data)

        cls.aggregated_data = aggregate(filter_platforms(data))

    def test_1_1_return_type(self):
        self.checkReturnType(self.fig, expected_type=plt.Figure)

    def test_1_2_number_of_axes(self):
        self.checkNumberOfAxes(self.fig.axes, expected_number=1)

    def test_1_3_pie_kind(self):
        self.checkNumberOfCollections(self.fig.axes[0], expected_number=0)
        self.checkNumberOfLines(self.fig.axes[0], 0)
        self.checkNumberOfContainers(self.fig.axes[0], 0)

        self.checkNumberOfPatches(self.fig.axes[0], 4)
        for i in range(4):
            self.checkPatchesType(self.fig.axes[0], Wedge, patch_number=i)

    def test_2_1_pie_position(self):
        self.checkPiePosition(self.fig.axes[0], expected_position=self.aggregated_data["count"].to_list())

    def test_2_2_pie_labels(self):
        self.checkPieLabels(self.fig.axes[0], expected_labels=self.aggregated_data["platform"].to_list())

    def test_2_3_pie_numeric_labels(self):
        expected_count = self.aggregated_data["count"]
        expected_count = expected_count / sum(expected_count) * 100
        expected_labels = expected_count.apply(lambda count: "%.2f%%" % count)  # noqa: UP031

        self.checkPieNumericLabels(
            self.fig.axes[0],
            expected_labels=expected_labels.to_list(),
        )

    def test_2_4_pie_colors(self):
        self.checkPieColors(self.fig.axes[0], expected_colors=["C0", "C1", "C2", "C3"])

    def test_3_title(self):
        self.checkTitle(self.fig.axes[0], None)
