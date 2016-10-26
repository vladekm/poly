"""Tests for Polygon"""
# pylint: disable=too-few-public-methods, no-self-use, missing-docstring

from unittest import TestCase
import mock

from .. import Polygon


class PolygonTestCase(TestCase):
    """Test Polygon setup"""
    def test_polygon_can_be_initialized_without_ports(self):
        # W a polygon is instantiated without params
        my_polygon = Polygon()
        # T the polygon is available
        self.assertTrue(my_polygon)

    def test_polygon_can_be_initialized_with_empty_ports(self):
        # W a polygon is instantiated with empty ports
        my_polygon = Polygon(provides=None, needs=None)
        # T the polygon is True
        self.assertTrue(my_polygon)

    def test_polygon_provides_api_as_its_attribute(self):
        # W a polygon is instantiated with a non empty api
        my_port = mock.Mock()
        my_polygon = Polygon(provides={'port1': my_port})
        # T the new api port is exposed as an attribute
        my_polygon.port1.get_potatoes('fresh', amount=3)
        # T the call to the api is made with provided args and kwargs
        my_port.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_access_to_missing_api_raises_attributeerror(self):
        # W a polygon is instantiated without an api
        my_polygon = Polygon()
        # W an non-existant API is accessed
        # T an AttributeError is raised
        with self.assertRaises(AttributeError):
            my_polygon.not_there

    def test_polygon_needs_port_is_not_accessible_as_attr(self):
        # G a polygon is instantiated with a needs port
        my_polygon = Polygon(needs={'needs1': None})
        # W the needs port is called on the polygon
        # T an AttributeError is raised
        with self.assertRaises(AttributeError):
            my_polygon.needs1

    def test_initialized_polygon_exposes_its_provides_ports_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides port
        mport1 = mock.Mock()
        mport2 = mock.Mock()
        my_polygon = Polygon(provides={'port1': mport1, 'port2': mport2})
        # T the polygon exposes the ports as a dictionary
        expected = {'port1': mport1, 'port2': mport2}
        self.assertEquals(expected, my_polygon.provides)

    def test_initialized_polygon_exposes_its_needs_ports_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides port
        mport1 = mock.Mock()
        mport2 = mock.Mock()
        my_polygon = Polygon(needs={'port1': mport1, 'port2': mport2})
        # T the polygon exposes the ports as a dictionary
        expected = {'port1': mport1, 'port2': mport2}
        self.assertEquals(expected, my_polygon.needs)

    def test_port_cannot_be_named_a_reserved_word(self):
        reserved_words = ['api', 'needs', 'provides']
        # W a Polygon is instantiated with a reserved word for a port name
        # T an exception is raised
        for word in reserved_words:
            with self.assertRaisesRegexp(
                AttributeError,
                "'{}' is a reserved word.".format(word)
            ):
                Polygon(needs={word: None, 'whatever': None})
            with self.assertRaisesRegexp(
                AttributeError,
                "'{}' is a reserved word.".format(word)
            ):
                Polygon(provides={word: None, 'whatever': None})

class PolygonFrameworkUtilsTestCase(TestCase):
    def test_polygon_can_be_repred(self):
        # W a polygon is instantiated with a non empty api
        my_port1 = mock.Mock()
        my_port2 = mock.Mock()
        my_polygon = Polygon(
            provides={'my_port1': my_port1},
            needs={'my_port2': my_port2}
        )
        my_repr = repr(my_polygon)
        # T the repr matches the expected value
        expected_repr = (
            "{}("
            "provides={}, "
            "needs={})"
            ""
        ).format(
            Polygon,
            {'my_port1': my_port1},
            {'my_port2': my_port2},
        )
        self.assertEquals(expected_repr, my_repr)
