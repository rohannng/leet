import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        # self.assertEqual(sol.int_to_roman(5), "V")
        # self.assertEqual(sol.int_to_roman(20), "XX")
        # self.assertEqual(sol.int_to_roman(8), "VIII")
        # self.assertEqual(sol.int_to_roman(4), "IV")
        # self.assertEqual(sol.int_to_roman(9), "IX")
        # self.assertEqual(sol.int_to_roman(40), "XL")
        # self.assertEqual(sol.int_to_roman(90), "XC")
        self.assertEqual(sol.int_to_roman(1994), "MCMXCIV")


if __name__ == '__main__':
    unittest.main()
