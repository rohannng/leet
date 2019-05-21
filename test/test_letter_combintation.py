import unittest

from solution import Solution


class TestSomething(unittest.TestCase):
    def test_letter_combination(self):
        sol = Solution()
        self.assertListEqual(sol.letterCombination("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


if __name__ == '__main__':
    unittest.main()
