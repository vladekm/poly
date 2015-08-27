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
        # G a polygon is instantiated with a non empty provides facet
        my_facet = mock.Mock()
        my_polygon = Polygon(provides={'facet1': my_facet})
        # W the new provides facet is exposed
        my_polygon.provides['facet1'].get_potatoes('fresh', amount=3)
        # T the call is made with provided args and kwargs
        my_facet.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_Polygon_is_initialized_and_facet_is_accessible_as_attr(self):
        # W a polygon is instantiated with a non empty provides facet
        my_facet = mock.Mock()
        my_polygon = Polygon(provides={'facet1': my_facet})
        # T the new provides facet is exposed
        my_polygon.facet1.get_potatoes('fresh', amount=3)
        # T the call is made with provided args and kwargs
        my_facet.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_initialized_Polygon_exposes_its_provides_facets_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides facet
        mfacet1 = mock.Mock()
        mfacet2 = mock.Mock()
        my_polygon = Polygon(provides={'facet1': mfacet1, 'facet2': mfacet2})
        # T the polygon exposes the facets as a dictionary
        expected = {'facet1': mfacet1, 'facet2': mfacet2}
        self.assertEquals(expected, my_polygon.provides)
