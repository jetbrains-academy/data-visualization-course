from typing import Any, List, Optional
from unittest import TestCase

from matplotlib.colors import same_color, to_rgb
from numpy.testing import assert_allclose, assert_array_almost_equal
from seaborn import FacetGrid


# TODO: error messages
# We're using camelCase here to be consistent with unittest
class BaseTestMixin(TestCase):
    def checkReturnType(self, obj: Any, function_name: Optional[str] = None):
        if function_name is None:
            error_message = "Use a figure-level function"
        else:
            error_message = f"Use the `{function_name}` function"

        self.assertIsInstance(obj, FacetGrid, error_message)

    def checkNumberOfAxes(self, fig: FacetGrid, expected_number: int):
        current_number = len(fig.axes.flat)
        self.assertEqual(
            expected_number,
            current_number,
            f"The figure must have only {expected_number} axes. Please check that you pass the right parameters",
        )

    def checkNumberOfCollections(self, fig: FacetGrid, expected_number: int):
        collections = getattr(fig.ax, "collections", [])
        self.assertEqual(
            expected_number,
            len(collections),
            msg=(
                f"The figure must have only {expected_number} collection objects. "
                f"Please check that you pass the right parameters"
            ),
        )

    # def checkCollectionType(self, fig: FacetGrid, expected_type: Type[plt.Collection], collection_number: int = 0):
    #     self.assertIsInstance(
    #         fig.ax.collections[collection_number],
    #         expected_type,
    #         f'The collection must have an instance of `{expected_type}`',
    #     )

    @staticmethod
    def checkCollectionPosition(
        fig: FacetGrid,
        expected_x: List[float],
        expected_y: List[float],
        collection_number: int = 0,
    ):
        actual_x, actual_y = fig.ax.collections[collection_number].get_offsets().T
        assert_array_almost_equal(actual_x, expected_x)
        assert_array_almost_equal(actual_y, expected_y)

    @staticmethod
    def checkCollectionTransparency(fig: FacetGrid, expected_transparency: float, collection_number: int = 0):
        assert_allclose(fig.ax.collections[collection_number].get_alpha(), expected_transparency)

    def checkCollectionColor(self, fig: FacetGrid, expected_facecolor: str, collection_number: int = 0):
        self.assertTrue(
            same_color(to_rgb(expected_facecolor), to_rgb(fig.ax.collections[collection_number].get_facecolor())),
        )

    def checkNumberOfLines(self, fig: FacetGrid, expected_number: int):
        lines = getattr(fig.ax, "lines", [])
        self.assertEqual(
            expected_number,
            len(lines),
            msg=(
                f"The figure must have only {expected_number} line objects. "
                f"Please check that you pass the right parameters"
            ),
        )

    @staticmethod
    def checkLinePosition(fig: FacetGrid, expected_x: List[float], expected_y: List[float], line_number: int = 0):
        actual_x, actual_y = fig.ax.lines[line_number].get_xydata().T
        assert_array_almost_equal(actual_x, expected_x)
        assert_array_almost_equal(actual_y, expected_y)

    @staticmethod
    def checkLineTransparency(fig: FacetGrid, expected_transparency: float, line_number: int = 0):
        actual_transparency = fig.ax.lines[line_number].get_alpha()
        if actual_transparency is None:
            # If alpha is None, then it by default equals 1
            actual_transparency = 1

        assert_allclose(actual_transparency, expected_transparency)

    def checkLineColor(self, fig: FacetGrid, expected_color: str, line_number: int = 0):
        self.assertTrue(same_color(to_rgb(expected_color), to_rgb(fig.ax.lines[line_number].get_color())))


# class RelplotTestMixin(ABC, TestCase):
#     @property
#     @abstractmethod
#     def kind(self) -> Literal['scatter', 'line']:
#         raise NotImplementedError
#
#     # TODO: make it better
#     def checkRelplotKind(self, fig: FacetGrid):
#         ax = fig.ax
#
#         collections_exists = getattr(ax, 'collections', None) is not None
#         lines_exists = getattr(ax, 'lines', None) is not None
#
#         if collections_exists and lines_exists:
#             actual_kind = 'line'
#         elif collections_exists:
#             actual_kind = 'scatter'
#         elif lines_exists:
#             actual_kind = 'line'
#         else:
#             actual_kind = None
#
#         self.assertIsNotNone(
#             actual_kind,
#             "Can't determine the kind of a figure. Use `seaborn.relational.relplot` for plotting",
#         )
#
#         self.assertEqual(
#             self.kind,
#             actual_kind,
#             f"The figure must be build a {self.kind} plot. Pass `kind='{self.kind}'` to the function",
#         )
#
#     def checkNumberOfTraces(self, fig: FacetGrid, expected_number: int):
#         if self.kind == 'scatter':
#             actual_number = len(fig.ax.collections)
#         else:
#             actual_number = len(fig.ax.lines)
#
#         self.assertEqual(
#             expected_number,
#             actual_number,
#             f'The number of traces on the figure must be exactly {expected_number}.',
#         )
#
#     def checkDataPosition(self, fig: FacetGrid, expected_x: List, expected_y: List):
#         if self.kind == 'scatter':
#             actual_x, actual_y = fig.ax.collections[0].get_offsets().T
#         else:
#             actual_x, actual_y = fig.ax.lines[0].get_xydata().T
#
#         # TODO: error messages
#         assert_array_almost_equal(actual_x, expected_x, err_msg='x')
#         assert_array_almost_equal(actual_y, expected_y, err_msg='y')
#
#     def checkTraceTransparency(self, fig: FacetGrid, expected_alpha: float):
#         if self.kind == 'scatter':
#             actual_alpha = fig.ax.collections[0].get_alpha()
#         else:
#             actual_alpha = fig.ax.lines[0].get_alpha()
#
#         if actual_alpha is None:
#             actual_alpha = 1.0
#
#         # TODO; error message
#         assert_allclose(expected_alpha, actual_alpha)
#
#     def checkTraceColor(self, fig: FacetGrid, expected_color: str):
#         expected_rgb = to_rgb(expected_color)
#
#         if self.kind == 'scatter':
#             actual_rgb = to_rgb(fig.ax.collections[0].get_facecolor())
#         else:
#             actual_rgb = to_rgb(fig.ax.lines[0].get_color())
#
#         self.assertTrue(same_color(expected_rgb, actual_rgb))
