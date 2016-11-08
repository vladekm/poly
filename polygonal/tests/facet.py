"""Tests for Facet"""
# pylint: disable = no-self-use, inherit-non-class, no-self-argument
# pylint: disable = missing-docstring

from unittest import TestCase
import mock

from .. import Facet


class FacetTestCase(TestCase):
    def test_facet_must_have_a_name(self):
        # W a facet is instantiated without a name
        # T an AttributeError is raised
        with self.assertRaises(TypeError):
            Facet()

    def test_facet_can_be_instantiated_without_ports(self):
        # W a facet is instantiated without ports
        my_facet = Facet('My facet')
        # T the facet is true
        self.assertTrue(my_facet)

    def test_facet_can_be_instantiated_with_empty_ports(self):
        # W a facet is instantiated with empty ports
        my_facet = Facet('My facet', ports=None)
        # T the facet is true
        self.assertTrue(my_facet)

    def test_facet_provides_ports_as_its_attribute(self):
        # W a facet is instantiated with a non empty port
        my_port = mock.Mock()
        my_facet = Facet('My facet', ports={'port1': my_port})
        # T the new api port is exposed as an attribute
        my_facet.port1.get_potatoes('fresh', amount=3)
        # T the call to the port is made with provided args and kwargs
        my_port.get_potatoes.assert_called_once_with('fresh', amount=3)

    def test_access_to_missing_port_raises_attributeerror(self):
        # W a facet is instantiated without a port
        my_facet = Facet('My facet')
        # W an non-existant API is accessed
        # T an AttributeError is raised
        with self.assertRaises(AttributeError):
            my_facet.not_there()

    def test_initialized_facet_exposes_its_ports_as_a_dict(self):
        # W a polygon is instantiated with a non empty provides port
        mport1 = mock.Mock()
        mport2 = mock.Mock()
        my_facet = Facet('My facet', ports={'port1': mport1, 'port2': mport2})
        # T the facet exposes the ports as a dictionary
        expected = {'port1': mport1, 'port2': mport2}
        self.assertEquals(expected, my_facet.ports)

    def test_port_cannot_be_named_a_reserved_word(self):
        reserved_words = ['api', 'needs', 'provides']
        # W a Facet is instantiated with a reserved word for a port name
        # T an exception is raised
        for word in reserved_words:
            with self.assertRaisesRegexp(
                AttributeError,
                "'{}' is a reserved word.".format(word)
            ):
                Facet('My facet', ports={word: None, 'whatever': None})
