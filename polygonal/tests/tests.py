"""Tests for the basic concepts"""
# pylint: disable=too-few-public-methods, no-self-use, missing-docstring

from unittest import TestCase
import mock

from zope.interface import Interface, implements

from ..exceptions import (
    UnadaptedPortException,
    BrokenInterfaceException,
    PortConfigurationException,
)
from .. import Port
from .. import Polygon


class PortInstantiationTestCase(TestCase):
    """TestCase for the port instantiation"""
    def setUp(self):
        """Generic test setup"""
        # G an interface
        class ITestInterface(Interface):

            def a_method(param1, param2=1):
                pass
        self.interface = ITestInterface

        # A a mock adapter
        class MyAdapter(object):
            implements(self.interface)

            def __init__(self):
                self.param1 = None
                self.param2 = None

            def a_method(self, param1, param2=1):
                self.param1 = param1
                self.param2 = param2
        self.adapter = MyAdapter()

    def test_port_can_be_repred(self):
        # G a port is instantiated with an interface and an adapter
        my_port = Port(self.interface, self.adapter)
        # W repr is generated
        my_repr = repr(my_port)
        # T the repr matches the expected value
        expected_repr = (
            "{}("
            "interface={}, "
            "adapter={})"
            "".format(Port, self.interface, self.adapter)
        )
        self.assertEquals(expected_repr, my_repr)

    def test_calling_port_adapted_on_instantiation_delegates_to_adapter(self):
        # G a port is instantiated with an interface and an adapter 
        my_port = Port(self.interface, self.adapter)
        # W I call the port on its interface
        my_port.a_method('a', param2=1)
        # T the adapter receives the call and the args and kwargs
        self.assertEquals('a', my_port.param1)
        self.assertEquals(1, my_port.param2)

    def test_call_port_plugged_post_instantiation_delegates_to_adapter(self):
        # G a port is instantiated without an adapter
        my_port = Port(self.interface)
        # G and an adapter is plugged into the port
        my_port.plug(self.adapter)
        # W I call the port on its interface
        my_port.a_method('a', param2=1)
        # T the adapter receives the call and the args and kwargs
        self.assertEquals('a', self.adapter.param1)
        self.assertEquals(1, self.adapter.param2)

    def test_port_without_interface_raises_exception(self):
        # W a port is instantiated without an interface
        # T a PortConfiguration exception is raised
        with self.assertRaises(PortConfigurationException):
            Port()


class PortAdaptationTestCase(TestCase):
    """Test Port and its interface"""

    def test_calling_port_with_unadapted_interface_raises_exception(self):
        # G an interface
        class MyPortInterface(Interface):
            def a_method(self):
                pass
        # G a port is instantiated
        my_port = Port(MyPortInterface)
        # W I access the unadapted interface
        # T PortConfiguration exception is raised
        with self.assertRaises(UnadaptedPortException):
            my_port.param1_method()

    def test_mistmatching_adapter_raises_brokeninterfaceexception(self):
        # G an interface
        class IPortInterface(Interface):
            def a_method(param1, param2=1):
                pass
        # A mistmatching adapters

        class AdapterWithoutAMethod(object):
            implements(IPortInterface)

        class AdapterWithABrokenMethod(object):
            implements(IPortInterface)

            def a_method(self):
                pass
        mismatching_adapters = [
            AdapterWithoutAMethod,
            AdapterWithABrokenMethod
        ]
        # A a port
        my_port = Port(IPortInterface)
        # W an adapter is plugged in
        # T the BrokenInterfaceException is raised
        for adapter in mismatching_adapters:
            with self.assertRaises(BrokenInterfaceException):
                my_port.plug(adapter())


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
