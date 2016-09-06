class FacetConfigurationException(Exception):
    """Facet is misconfigured"""

class UnadaptedPortException(FacetConfigurationException):
    """Port is not adapted"""

class BrokenInterfaceException(FacetConfigurationException):
    """Adapter does not match the port"""
