"""Definition of Facet"""

RESERVED_WORDS = ['api', 'needs', 'provides']


class Facet(object):
    """Facet collects the ports and organises them as a namespace"""
    def __init__(self, name, ports=None):
        self.name = name
        ports = ports or {}
        for key in ports:
            if key in RESERVED_WORDS:
                raise AttributeError(
                    "'{}' is a reserved word.".format(key)
                )
        self.ports = ports

    def __getattr__(self, *args, **kwargs):
        potential_port_name = args[0]
        if self.ports and potential_port_name in self.ports:
            return self.ports[potential_port_name]
        raise AttributeError()
