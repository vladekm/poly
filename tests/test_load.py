import unittest
from polygons import Load, UnadaptedFacet, BrokenInterface


class FakeAdapter(object):
    pass


class LoadTestCase(unittest.TestCase):
    def test_call_to_unadapted_facet_raises(self):
        myload = Load()
        with self.assertRaises(UnadaptedFacet):
            myload.provides['input'].create()

    def test_call_to_adapted_facet_raises_on_broken_interface(self):
        myload = Load()
        with self.assertRaises(BrokenInterface):
            myload.provides['input'].plug(FakeAdapter())

    #def test_call_to_needed_facet_fails(self):
        #myload = Load()
        #with self.assertRaises(Exception):
            #myload.input.create()

