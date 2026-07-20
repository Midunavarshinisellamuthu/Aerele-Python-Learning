import unittest
from calculator import add, sub


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 4), 14)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)


if __name__ == "__main__":
    unittest.main()
