#class ILoadInput(IFacet):
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


class Polygon(object):
    """Holds the configuration of facets and allows for instantiation of
    a polygon and the core providing the logic.

    Expects to be provided with a definition of all the facets's on construction
    Expects adapters and the core on instantiation.
    The core is a first class citizen and no checks are being done on it.
    Adapter checks are delegated to the facets.
    """
    facets = {}
    def __new__(cls, interfaces):
        import pdb; pdb.set_trace()
        conf = cls.parse_config(interfaces)
        for facet in conf:
            cls.facets[facet.name] = Facet(facet.conf)
        return cls

    def __init__(self, adapters, core):
        import pdb; pdb.set_trace()
        for adapter in adapters:
            self.facet[adapter.name].plug(adapter)
        self.core = core

    @classmethod
    def parse_config(cls, interfaces):
        return interfaces
        


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


class Load(Polygon):
    def __init__(self, provides=None, needs=None):
        for provide in provides:
            self.incoming_facets.add(Facet(provide))
        for need in needs:
            self.outgoing_facets.add(Facet(need))


myPol = Polygon({'interface_name': 'interface_content'})
import pdb; pdb.set_trace()
