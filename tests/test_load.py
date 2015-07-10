import unittest
from polygons import Load


class LoadTestCase(unittest.TestCase):
    myload = Load()
    myload.create('name')
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    unittest.main()
