import unittest
import pdb; pdb.set_trace()
from polygons import Monogon


class MonogonTestCase(unittest.TestCase):
    def test_call_to_create_succeeds(self):
        my_gon = Monogon()
        my_gon.create('name')


if __name__ == '__main__':
    unittest.main()
