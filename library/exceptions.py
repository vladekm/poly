class FacetConfigurationException(Exception):
    """Facet is misconfigured"""

class UnadaptedPortException(FacetConfigurationException):
    """Port is not adapted"""
