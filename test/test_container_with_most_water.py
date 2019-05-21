import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    sol = Solution()

    def test_something(self):
        anser = self.sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        assert anser == 49


if __name__ == '__main__':
    unittest.main()
