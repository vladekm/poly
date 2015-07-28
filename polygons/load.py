import uuid


class Polygon(object):
    """Holds the configuration of facets and allows for instantiation of
    a polygon and the core providing the logic.

    Expects to be provided with a definition of all the facets's on construction
    Expects adapters and the core on instantiation.
    The core is a first class citizen and no checks are being done on it.
    Adapter checks are delegated to the facets.
    """
    needs = {}
    provides = {}
    core = None

    def __init__(self, provides=None, needs=None):
        if provides is None:
            provides = self.provides
        if needs is None:
            needs = self.needs
        for key, facet in provides.items():
            self.provides[key] = Facet(facet)
        for key, facet in needs.items():
            self.needs[key] = Facet(facet)

    def __getattr__(self, *args, **kwargs):
        for attr in args:
            if attr in self.provides:
                return self.provides[attr]

class Load(Polygon):
    needs = {}
    provides = {
        'input':{
            '_name_': 'IInput',
            'create': {
                'name': str,
                'weight': int,
                'uuid': uuid.UUID,
            },
            'read': {
                'uuid': uuid.UUID,
            },
            'update': {
                'name': str,
                'weight': int,
                'uuid': uuid.UUID,
            },
            'delete': {
                'uuid': uuid.UUID,
            }
        }
    }


class UnadaptedFacet(Exception):
    pass


class Facet(object):
    """Holds the definition of the specific interface and allows for the adapters to be plugged in.

    Expects a definition of a facet on instantiantion.
    Accepts adapters and does the basic check of adapter's conformity to the interface
    """
    def __init__(self, interface):
        self.interface = interface

    def plug(self, adapter):
        if self.check_interface(adapter):
            self.adapter = adapter

    def check_interface(self, adapter):
        return True

    def __getattr__(self, attr):
        if attr in self.interface:
            return self.interface[attr]


#class ILoadInput(zope.interface.Interface):
    #def create():
        #pass

    #def read():
        #pass

    #def update():
        #pass

    #def delete():
        #pass


#class ILoadCRUD(IFacet):
    #def create():
        #pass

    #def read():
        #pass

    #def update():
        #pass

    #def delete():
        #pass


