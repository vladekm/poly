"""Port related Test Cases"""
# pylint: disable=too-few-public-methods, no-self-use, missing-docstring
# pylint: disable=inherit-non-class, no-self-argument
from unittest import TestCase

from zope.interface import Interface, implements

from .. import Port
from ..exceptions import (
    UnadaptedPortException,
    BrokenInterfaceException,
    PortConfigurationException,
)


class PortTestCaseBase(TestCase):
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


class PortFrameworkUtilsTestCase(PortTestCaseBase, TestCase):
    """TestCase framework helpers."""

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


class PortInstantiationTestCase(PortTestCaseBase):
    """TestCase for the port instantiation"""
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
