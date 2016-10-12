"""Exceptions for use with the framework"""


class PortConfigurationException(Exception):
    """Port is misconfigured"""


class UnadaptedPortException(PortConfigurationException):
    """Port is not adapted"""


class BrokenInterfaceException(PortConfigurationException):
    """Adapter does not match the port"""
