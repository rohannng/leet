import unittest

from solution import Solution
from util import build_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        lst = [1]

        head = build_list(lst)

        end = sol.remove_nth_from_list_end(head, 1)



        if __name__ == '__main__':
            unittest.main()
