import unittest
from polygons import Load, UnadaptedFacet


class LoadTestCase(unittest.TestCase):
    def test_call_to_unadapted_facet_raises(self):
        myload = Load()
        with self.assertRaises(UnadaptedFacet):
            myload.provides['input'].create()

    #def test_call_to_provided_facet_succeeds(self):
        #myload = Load()
        #assert myload.input.create()

    #def test_call_to_needed_facet_fails(self):
        #myload = Load()
        #with self.assertRaises(Exception):
            #myload.input.create()

