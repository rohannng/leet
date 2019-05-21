import unittest

from solution import Solution


class MyTest(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(sol.roman_to_int("X"), 10)
        self.assertEqual(sol.roman_to_int("LVIII"), 58)
        self.assertEqual(sol.roman_to_int("IX"), 9)
        self.assertEqual(sol.roman_to_int("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
