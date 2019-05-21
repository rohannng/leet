import unittest

from solution import Solution
from util import build_list, arr_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        l1 = build_list([1, 3, 5])
        l2 = build_list([2, 4, 6])
        self.assertListEqual(arr_list(sol.merge_two_sorted_list(l1, l2)), [1, 2, 3, 4, 5, 6])

        l1 = build_list([1,])
        l2 = build_list([2, 4, 6])
        self.assertListEqual(arr_list(sol.merge_two_sorted_list(l1, l2)), [1, 2, 4, 6])

        l1 = build_list([])
        l2 = build_list([])
        self.assertListEqual(arr_list(sol.merge_two_sorted_list(l1, l2)), [''])

        l1 = build_list([1,2,4])
        l2 = build_list([1,3,4])
        self.assertListEqual(arr_list(sol.merge_two_sorted_list(l1, l2)), [1,1,2,3,4,4])



if __name__ == '__main__':
    unittest.main()
