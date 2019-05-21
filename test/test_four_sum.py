import unittest

from solution import Solution


class TestFourSum(unittest.TestCase):
    def test_four_sum(self):
        sol = Solution()
        self.assertListEqual(sol.four_sum([1, 0, -1, 0, -2, 2], 0), [
            [-1, 0, 0, 1],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2]
        ])


if __name__ == '__main__':
    unittest.main()
