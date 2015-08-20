'''Definition of the base Polygon'''
from .facet import Facet


class Polygon(object):
    """Holds the configuration of facets and allows for instantiation of
    a polygon and the core providing the logic.

    Expects to be provided with a definition of all the facets's on construction
    Expects adapters and the core on instantiation.
    nThe core is a first class citizen and no checks are being done on it.
    Adapter checks are delegated to the facets.
    """
    def __init__(self, provides=None, needs=None):
        self.provides = {}
        self.needs = {}
        for key, facet in provides.items():
            self.provides[key] = Facet(facet)
        for key, facet in needs.items():
            self.needs[key] = Facet(facet)

    def call(self, facet, method, *args, **kwargs):
        """Call the polygon on specified facet.

        :param string facet: string representation of the facet to be
            called
        :param string method: string representation of the method to
            be executed
        :param *args, **kwargs: will be passed on to the facet method

        """
        method = self.provides[facet][method]
        return method(*args, **kwargs)
