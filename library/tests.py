import mock

from unittest import TestCase
from zope import interface

from .exceptions import (
    BrokenInterfaceException,
    PortConfigurationException,
    UnadaptedPortException,
)
from .port import Port
from .polygon import Polygon


class PortInstantiationTestCase(TestCase):
    def setUp(self):
        # G an interface
        class ITestInterface(interface.Interface):
            def a_method(a, b=1):
                pass
        self.interface = ITestInterface
        # A a mock adapter
        class MyAdapter(object):
            interface.implements(self.interface)
            def a_method(self, a, b=1):
                self.a = a
                self.b = b
        self.adapter = MyAdapter()

    def test_calling_port_adapted_on_instantiation_delegates_to_adapter(self):
        # G a port is instantiated with a behaviour definition
        my_port = Port(self.interface, self.adapter)
        # W I call the port on its interface
        my_port.a_method('a', b=1)
        # T the adapter receives the call and the args and kwargs
        self.assertEquals('a', my_port.a)
        self.assertEquals(1, my_port.b)

    def test_calling_port_plugged_post_instantiation_delegates_to_adapter(self):
        # G a port is instantiated 
        my_port = Port(self.interface, self.adapter)
        # W I call the port on its interface
        my_port.a_method('a', b=1)
        # T the adapter receives the call and the args and kwargs
        self.assertEquals('a', self.adapter.a)
        self.assertEquals(1, self.adapter.b)

    def test_port_without_interface_raises_Exception(self):
        # W a port is instantiated without an interface
        # T a PortConfiguration exception is raised
        with self.assertRaises(PortConfigurationException):
            Port()


class PortAdaptationTestCase(TestCase):
    """Test Port and its interface"""

    def test_calling_port_with_unadapted_interface_raises_Exception(self):
        # G an interface
        class MyPortInterface(interface.Interface):
            def a_method():
                pass
        # G a port is instantiated
        my_port = Port(MyPortInterface)
        # W I access the unadapted interface
        # T PortConfiguration exception is raised 
        with self.assertRaises(UnadaptedPortException):
            my_port.a_method()

    def test_adapter_mismatching_the_port_raises_BrokenInterfaceException(self):
        # G an interface
        class IPortInterface(interface.Interface):
            def a_method(a, b=1):
                pass
        # A an adapter
        class MyAdapter(object):
            def a_method(self, a):
                pass
        # Asa port
        my_port = Port(IPortInterface)
        # W the adapter is plugged in
        # T the BrokenInterfaceException is raised
        with self.assertRaises(BrokenInterfaceException):
            my_port.plug(MyAdapter())


class PolygonTestCase(TestCase):
    """Test Polygon setup"""
    def test_Polygon_is_initialized_without_ports_correctly(self):
        # W a polygon is instantiated without params
        my_polygon = Polygon()
        # T the polygon is True
        self.assertTrue(my_polygon)

    def test_Polygon_is_initialized_with_empty_ports_correctly(self):
        # W a polygon is instantiated with empty ports
        my_polygon = Polygon(provides=None, needs=None)
        # T the polygon is True
        self.assertTrue(my_polygon)

    def test_Polygon_is_initialized_with_non_empty_provides(self):
        # G a polygon is instantiated with a non empty provides port
        my_port = mock.Mock()
        my_polygon = Polygon(provides={'port1': my_port})
        # W the new provides port is exposed
        my_polygon.provides['port1'].get_potatoes('fresh', amount=3)
        # T the call is made with provided args and kwargs
        my_port.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_Polygon_provides_port_is_accessible_as_attr(self):
        # W a polygon is instantiated with a non empty provides port
        my_port = mock.Mock()
        my_polygon = Polygon(provides={'port1': my_port})
        # T the new provides port is exposed
        my_polygon.port1.get_potatoes('fresh', amount=3)
        # T the call is made with provided args and kwargs
        my_port.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_Polygon_needs_port_is_not_accessible_as_attr(self):
        # G a polygon is instantiated with a non empty provides port
        my_port = mock.Mock()
        my_polygon = Polygon(needs={'needs1': my_port})
        # W the needs port is called on the polygon
        # T the exception is raised
        # TODO: Decide on the exception
        with self.assertRaises(Exception):
            my_polygon.needs1.get_potatoes('fresh', amount=3)

    def test_initialized_Polygon_exposes_its_provides_ports_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides port
        mport1 = mock.Mock()
        mport2 = mock.Mock()
        my_polygon = Polygon(provides={'port1': mport1, 'port2': mport2})
        # T the polygon exposes the ports as a dictionary
        expected = {'port1': mport1, 'port2': mport2}
        self.assertEquals(expected, my_polygon.provides)

    def test_initialized_Polygon_exposes_its_needs_ports_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides port
        mport1 = mock.Mock()
        mport2 = mock.Mock()
        my_polygon = Polygon(needs={'port1': mport1, 'port2': mport2})
        # T the polygon exposes the ports as a dictionary
        expected = {'port1': mport1, 'port2': mport2}
        self.assertEquals(expected, my_polygon.needs)

    def test_port_cannot_be_named_a_reserved_word(self):
        RESERVED_WORDS = ['needs', 'provides']
        # W a Polygon is instantiated with a reserved word for a port name
        # T an exception is raised
        for word in RESERVED_WORDS:
            with self.assertRaises(Exception):
                Polygon(needs={word: None, 'whatever': None})

