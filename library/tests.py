from unittest import TestCase
import mock
from zope import interface

from .polygon import Polygon
from .facet import Facet
from .exceptions import FacetConfigurationException, UnadaptedPortException


class FacetTestCase(TestCase):
    """Test Facet and its interface"""
    def test_port_without_interface_raises_Exception(self):
        # W a facet is instantiated without an interface
        # T a FacetConfiguration exception is raised
        with self.assertRaises(FacetConfigurationException):
            Facet()

    def test_port_with_unadapted_interface_raises_Exception(self):
        # G an interface
        class MyFacetInterface(interface.Interface):
            def a_method():
                pass
        # G a facet is instantiated with a behaviour definition
        my_facet = Facet(MyFacetInterface)
        # T FacetConfiguration exception is raised on an unadapted interface access
        with self.assertRaises(UnadaptedPortException):
            my_facet.a_method()

    def test_calling_port_delegates_to_adapter(self):
        # G an interface
        class MyFacetInterface(interface.Interface):
            def a_method():
                pass
        # A a mocked adapter
        class MyAdapter(object):
            def a_method(self):
                pass
        my_adapter = mock.Mock(autospec=MyAdapter)
        # G a facet is instantiated with a behaviour definition
        my_facet = Facet(MyFacetInterface, MyAdapter())
        # W I call the port on its interface
        my_facet.a_method()
        # T the adapter receives the call and the args and kwargs
        my_adapter.called_once()



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

    def test_initialized_Polygon_exposes_its_needs_facets_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides facet
        mfacet1 = mock.Mock()
        mfacet2 = mock.Mock()
        my_polygon = Polygon(needs={'facet1': mfacet1, 'facet2': mfacet2})
        # T the polygon exposes the facets as a dictionary
        expected = {'facet1': mfacet1, 'facet2': mfacet2}
        self.assertEquals(expected, my_polygon.needs)

