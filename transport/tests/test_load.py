"""Tests for the Polygons used for the service"""
import unittest

from ...polygonal.polygons import Monogon


class MonogonTestCase(unittest.TestCase):
    """Can create a monogon"""
    def test_call_to_create_succeeds(self):
        """call to create succeeds"""
        my_gon = Monogon()
        my_gon.create()
        # TODO: this is totally broken

