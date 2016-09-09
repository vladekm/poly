'''Definition of the base Port'''
from zope.interface.verify import verifyClass
from zope.interface.exceptions import DoesNotImplement

from .exceptions import (
    BrokenInterfaceException,
    PortConfigurationException,
    UnadaptedPortException,
)


class Port(object):
    """Holds the definition of the specific interface and allows for the adapters to be plugged in.

    Expects a definition of a port on instantiantion.
    Accepts adapters and does the basic check of adapter's conformity to the interface
    """
    def __init__(self, interface=None, adapter=None):
        if not (interface):
            raise PortConfigurationException()
        self.adapter = None
        self.interface = interface
        if adapter:
            self.plug(adapter)

    def __getattr__(self, name):
        if not self.adapter:
            raise UnadaptedPortException('This port has no adapter')
        attr = getattr(self.adapter, name)
        return attr

    def plug(self, adapter):
        """plug adapter into the port

        :param adapter adapter: the adapter to be plugged in
        """
        try:
            verifyClass(self.interface, adapter.__class__)
        except DoesNotImplement as e:
            raise BrokenInterfaceException(e)
        self.adapter = adapter
