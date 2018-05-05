import unittest

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("Run once before all the test methods into the class")
    def setUp(self):
        pass

    def test_caseA(self):
        print ("test A")
    def test_caseB(self):
        print("test B")

    def tearDown(self):
        print ("clean the result")
    @classmethod
    def tearDownClass(cls):
        print ("Run once after execution of all the test methodes into class ")

if __name__ == '__main__':
    unittest.main(verbosity=2)
