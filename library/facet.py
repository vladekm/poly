'''Definition of the base Facet'''
from zope.interface.verify import verifyClass
from zope.interface.exceptions import DoesNotImplement

from .exceptions import (
    BrokenInterfaceException,
    FacetConfigurationException,
    UnadaptedPortException,
)


class Facet(object):
    """Holds the definition of the specific interface and allows for the adapters to be plugged in.

    Expects a definition of a facet on instantiantion.
    Accepts adapters and does the basic check of adapter's conformity to the interface
    """
    def __init__(self, interface=None, adapter=None):
        self.adapter = adapter
        if not (interface):
            raise FacetConfigurationException()
        self.interface = interface

    def __getattr__(self, name):
        if not self.adapter:
            raise UnadaptedPortException('This facet has no adapter')
        attr = getattr(self.adapter, name)
        return attr

    def plug(self, adapter):
        """plug adapter into the facet

        :param adapter adapter: the adapter to be plugged in
        """
        try:
            verifyClass(self.interface, adapter.__class__)
        except DoesNotImplement as e:
            raise BrokenInterfaceException
        self.adapter = adapter


class Facet_Old(object):
    def __init__(self, interface):
        self.__dict__['interface'] = interface['interface']


