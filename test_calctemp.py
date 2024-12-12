import unittest
from calctemp import celsius_para_fahrenheit

class TestCalculadora(unittest.TestCase):

    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_para_fahrenheit(25), 77, places=2)  # Tolerância para arredondamento

if __name__ == "__main__":
    unittest.main()