from calculator import *
import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(1024, 256), 1280)
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
    
    def test_subtract(self):
        self.assertEqual(subtract(635, 245), 390)
        self.assertEqual(subtract(45, 324), -279)
        self.assertEqual(subtract(943, 43), 900)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertEqual(logarithm(2, 64), 6)
        self.assertEqual(logarithm(3, 81), 4)
    
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)

if __name__=="__main__":
    unittest.main()
