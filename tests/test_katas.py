import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(3, 5), 8)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-4, -7), -11)
        self.assertEqual(katas.add(14, 21), 35)

    def test_multiply(self):
        self.assertEqual(katas.multiply(3, 5), 15)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(-4, -7), 28)
        self.assertEqual(katas.multiply(14, 21), 294)

    def test_power(self):
        self.assertEqual(katas.power(3, 5), 243)
        self.assertEqual(katas.power(10, 6), 1000000)
        self.assertEqual(katas.power(8, 2), 64)
        self.assertEqual(katas.power(2, 12), 4096)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(7), 5040)
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(2), 2)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(8), 13)
        self.assertEqual(katas.fibonacci(10), 34)
        self.assertEqual(katas.fibonacci(2), 1)


if __name__ == '__main__':
    unittest.main()
