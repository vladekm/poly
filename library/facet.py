'''Definition of the base Facet'''
from zope.interface.verify import verifyClass


class UnadaptedFacet(Exception):
    """Raised on calls to unadapted facets"""


class Facet(object):
    """Holds the definition of the specific interface and allows for the adapters to be plugged in.

    Expects a definition of a facet on instantiantion.
    Accepts adapters and does the basic check of adapter's conformity to the interface
    """
    def __init__(self, interface):
        self.adapter = None
        self.__dict__['interface'] = interface['interface']

    def plug(self, adapter):
        """plug adapter into the facet

        :param adapter adapter: the adapter to be plugged in
        """
        verifyClass(self.interface, adapter.__class__)
        self.adapter = adapter

    def __getattr__(self, attr):
        if not self.adapter:
            raise UnadaptedFacet('This facet has no adapter')

    def __getitem__(self, name):
        attr = getattr(self.adapter, name)
        return attr
