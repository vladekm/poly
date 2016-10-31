'''Definition of the base Polygon'''
RESERVED_WORDS = ['api', 'needs', 'provides']


class Polygon(object):
    """Holds the configuration of ports and allows for instantiation of
    a polygon and the core providing the logic.

    Expects to be provided with a definition of all the ports's on construction
    Expects adapters and the core on instantiation.
    The core is a first class citizen and no checks are being done on it.
    Adapter checks are delegated to the ports.
    """
    def __init__(self, provides=None, needs=None, core=None):
        provides = provides or {}
        needs = needs or {}
        for key in list(needs.keys() + provides.keys()):
            if key in RESERVED_WORDS:
                raise AttributeError(
                    "'{}' is a reserved word.".format(key)
                )
        self.provides = provides
        self.needs = needs
        if core:
            my_core = core()
            self._add_core(my_core)


    def __getattr__(self, *args, **kwargs):
        potential_port_name = args[0]
        if self.provides and potential_port_name in self.provides:
            return self.provides[potential_port_name]
        raise AttributeError()

    def __repr__(self):
        return (
            "{}("
            "provides={}, "
            "needs={})"
            "".format(Polygon, self.provides, self.needs)
        )

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

    def add_core(self, core):
        self._add_core(core)

    def _add_core(self, core):
        for port in self.provides.values():
            port.plug(core)
