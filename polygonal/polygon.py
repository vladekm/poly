'''Definition of the base Polygon'''
RESERVED_WORDS = ['needs', 'provides']


class Polygon(object):
    """Holds the configuration of ports and allows for instantiation of
    a polygon and the core providing the logic.

    Expects to be provided with a definition of all the ports's on construction
    Expects adapters and the core on instantiation.
    The core is a first class citizen and no checks are being done on it.
    Adapter checks are delegated to the ports.
    """
    def __init__(self, provides=None, needs=None):
        self.provides = provides or {}
        self.needs = needs or {}
        for key in self.needs.keys():
            if key in RESERVED_WORDS:
                raise Exception("OMG this port name is a reserver word")
        for key in self.provides.keys():
            if key in RESERVED_WORDS:
                raise Exception("OMG this port name is a reserver word")

    def __getattr__(self, *args, **kwargs):
        potential_port_name = args[0]
        if self.provides and potential_port_name in self.provides:
            return self.provides[potential_port_name]

    def call(self, port, method, *args, **kwargs):
        """Call the polygon on specified port.

        :param string port: string representation of the port to be
            called
        :param string method: string representation of the method to
            be executed
        :param *args, **kwargs: will be passed on to the port method

        """
        method = self.provides[port][method]
        return method(*args, **kwargs)
