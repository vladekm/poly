from . import Facet


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

    #def __getattr__(self, *args, **kwargs):
        #for attr in args:
            #if attr in self.provides:
                #return self.provides[attr]
        #return super(Polygon, self).__getattr__(*args, **kwargs)

    def call(self, facet, method, *args, **kwargs):
        method = self.provides[facet][method]
        return method(*args, **kwargs)
