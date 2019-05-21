import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(sol.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(sol.threeSumClosest([1, 1, 1, 0], -100), 2)
        self.assertEqual(sol.threeSumClosest([-3, -2, -5, 3, -4], -1),-2)


if __name__ == '__main__':
    unittest.main()
