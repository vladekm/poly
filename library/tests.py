from unittest import TestCase
import mock

from .polygon import Polygon


class PolygonTestCase(TestCase):
    """Test Polygon setup"""
    def test_Polygon_is_initialized_without_facets_correctly(self):
        # W a polygon is instantiated without params
        my_polygon = Polygon()
        # T the polygon is True
        self.assertTrue(my_polygon)

    def test_Polygon_is_initialized_with_empty_facets_correctly(self):
        # W a polygon is instantiated with empty facets
        my_polygon = Polygon(provides=None, needs=None)
        # T the polygon is True
        self.assertTrue(my_polygon)

    def test_Polygon_is_initialized_with_non_empty_provides(self):
        # W a polygon is instantiated with a non empty provides facet
        my_facet = mock.Mock()
        my_polygon = Polygon(provides={'facet1': my_facet})
        # then the new provides facet is exposed
        my_polygon.facet1.get_potatoes('fresh', amount=3)
        # and the call is made with provided args and kwargs
        my_facet.get_potatoes.assert_called_once_with('fresh', amount=3)

