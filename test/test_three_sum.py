import unittest

from solution import Solution


class MyTest(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertListEqual(sol.three_sum([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])


if __name__ == "__main__":
    unittest.main()
