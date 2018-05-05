import unittest
from  Include.SwapanTest1.Rectracngle import Rectrangle
class TestRectrangle(unittest.TestCase):

    def test_area(self):
        r=Rectrangle(4,5)
        self.assertEqual(r.area(), 20)
