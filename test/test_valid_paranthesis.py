import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(sol.valid_paranthesis("()"), True)
        self.assertEqual(sol.valid_paranthesis("(]"), False)
        self.assertEqual(sol.valid_paranthesis("()[]{}"), True)
        self.assertEqual(sol.valid_paranthesis("([)]"), False)
        self.assertEqual(sol.valid_paranthesis("{[]}"), True)



if __name__ == '__main__':
    unittest.main()
