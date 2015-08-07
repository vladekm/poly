from mock import Mock
import unittest
import zope.interface as interface
from zope.interface.exceptions import BrokenImplementation

from polygons import Monogon, UnadaptedFacet
from polygons import IMonogonProvides


class BrokenAdapter(object):
    interface.implements(IMonogonProvides)
    pass


class FakeAdapter(object):
    interface.implements(IMonogonProvides)
    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass


class PolygonTestCase(unittest.TestCase):
    def test_call_to_unadapted_facet_raises(self):
        my_polygon = Monogon()
        with self.assertRaises(UnadaptedFacet):
            my_polygon.provides['input'].create()

    def test_call_to_adapted_facet_raises_on_broken_interface(self):
        my_polygon = Monogon()
        with self.assertRaises(BrokenImplementation):
            my_polygon.provides['input'].plug(BrokenAdapter())

    def test_call_to_adapted_facet_calls_adapters_method(self):
        my_polygon = Monogon()
        fake_adapter = Mock(spec_set=FakeAdapter, name='MockFakeAdapter')
        my_polygon.provides['input'].plug(fake_adapter)
        my_polygon.call('input', 'create', 'a', 'b', 'c')
        fake_adapter.create.assert_called_once_with('a', 'b', 'c')


class LoadTestCase(unittest.TestCase):
    pass
        

    #def test_call_to_needed_facet_fails(self):
        #myload = Load()
        #with self.assertRaises(Exception):
            #myload.input.create()

