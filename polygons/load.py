import zope.interface as interface
from zope.interface.verify import verifyClass


class IMonogonProvides(interface.Interface):
    def create():
        pass

    def read():
        pass

    def update():
        pass

    def delete():
        pass


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


class Monogon(Polygon):
    def __init__(self):
        needs = {}
        provides = {
            'input':{
                'interface': IMonogonProvides,
            }
        }
        super(Monogon, self).__init__(provides, needs)


class UnadaptedFacet(Exception):
    pass


class BrokenInterface(Exception):
    pass


class Facet(object):
    """Holds the definition of the specific interface and allows for the adapters to be plugged in.

    Expects a definition of a facet on instantiantion.
    Accepts adapters and does the basic check of adapter's conformity to the interface
    """
    def __init__(self, interface):
        self.adapter = None
        self.__dict__['interface'] = interface['interface']

    def plug(self, adapter):
        verifyClass(self.interface, adapter.__class__)
        self.adapter = adapter

    def __getattr__(self, attr):
        if not self.adapter:
            raise UnadaptedFacet('This facet has no adapter')

    def __getitem__(self, name):
        attr = getattr(self.adapter, name);
        return attr
