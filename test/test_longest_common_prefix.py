import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(sol.longest_common_prefix(["abc", "ab", "d"]), "")
        self.assertEqual(sol.longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(sol.longest_common_prefix([]), "")


if __name__ == '__main__':
    unittest.main()
