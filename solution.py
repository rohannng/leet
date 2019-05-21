import collections
import sys

from util import ListNode


class Solution:
    @classmethod
    def longest_common_prefix(cls, strs):
        if not strs:
            return ""

        small = min(strs)
        big = max(strs)

        for i, c in enumerate(small):
            if big[i] != c:
                return small[:i]

        return small

    @classmethod
    def roman_to_int(cls, roman):
        mapping = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                   'D': 500,
                   'CM': 900, 'M': 1000}

        numeral = 0
        left_ptr = 0
        while left_ptr < len(roman):
            # if left_ptr + 1 < len(roman) and roman[left_ptr:left_ptr + 2] in mapping:
            #     numeral += mapping[roman[left_ptr:left_ptr + 2]]
            #     left_ptr += 2
            #     continue
            #
            # numeral += mapping[roman[left_ptr]]
            # left_ptr += 1
            numeral += mapping[roman[left_ptr]]
            # if preceding roman char is lesser than value than the current one then
            # that mean it is one of the special cases and we need to subtract
            # it twice to account for special case and the fact that we included it
            # in the total sum in the previous pass
            if left_ptr > 0 and mapping[roman[left_ptr - 1]] < mapping[roman[left_ptr]]:
                numeral -= 2 * mapping[roman[left_ptr - 1]]
            left_ptr += 1

        return numeral

    @classmethod
    def int_to_roman(cls, number):
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        result = ""

        int_desc = sorted(mapping.keys(), reverse=True)
        for amt in int_desc:
            while number >= amt:
                result += mapping[amt]
                number = number - amt

            # # Handle 6 exceptions
            # less = amt - number
            # if less in mapping and amt / less in (5, 10):
            #     result = result + mapping[less] + mapping[amt]
            #     number = 0

        return result

    @classmethod
    def max_area(cls, heights):
        """
        Given a list of wall heights - calculate the largest area of
        water held within the walls

        Start from both ends and converge in the following manner


        :param heights:
        :return: area
        """
        max_area = 0
        left_ptr = 0
        right_ptr = len(heights) - 1

        while left_ptr < right_ptr:
            # Update area
            max_area = max(max_area,
                           (right_ptr - left_ptr) *
                           (heights[left_ptr] if heights[left_ptr] < heights[right_ptr] else heights[right_ptr]))

            # Move pointers
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area

    @classmethod
    def three_sum(cls, nums):
        """

        :param nums:
        :return: list of
        """
        ans = set()
        for i, lft in enumerate(nums):
            track = {}
            for j, rt in enumerate(nums[i + 1:]):
                two_sum = lft + rt
                # need negative for 0
                if -two_sum in track:
                    ans.add(tuple(sorted([lft, rt, -two_sum])))
                else:
                    track[rt] = 1
        return list(ans)

    @classmethod
    def threeSumClosest(cls, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        closest = None

        # for i, lt in enumerate(nums):
        #     track = {}
        #     for j, rt in enumerate(nums[i + 1:]):
        #         if target - (lt + rt) in track:
        #             return target
        #         else:
        #             track[rt] = 1
        #             for k, rt2 in enumerate(nums[i + j + 2:]):
        #                 summ = lt + rt + rt2
        #                 closest = summ if (closest is None or abs(target - summ) < abs(target - closest)) else closest
        #                 print(lt, rt, rt2, lt + rt + rt2, target, closest)
        # return closest

        # using sort and then converging
        nums.sort()
        for i in range(len(nums) - 2):
            lt = i + 1
            rt = len(nums) - 1
            while lt < rt:
                summ = nums[i] + nums[lt] + nums[rt]
                if summ == target:
                    return target
                if summ < target:
                    lt += 1
                else:
                    rt -= 1

                if closest is None or abs(target - summ) < abs(target - closest):
                    closest = summ

        return closest

    @classmethod
    def letterCombination(cls, digits):

        if not digits:
            return []
        digit_dict = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqr",
                      "8": "stu",
                      "9": "vwxy"}

        result = []

        for d in digits:
            if not result:
                result = list(digit_dict[d])
            else:
                new_res = []
                for res in result:
                    for ch in digit_dict[d]:
                        new_res.append(res + ch)
                result = new_res
        return result

    @classmethod
    def four_sum(cls, nums, target):
        """
        USe Recursion with base case as two sum problem
        # recursion
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return []

        res = set()
        for i, lft in enumerate(nums):
            for j, lft1 in enumerate(nums[i + 1:]):
                track1 = collections.defaultdict(list)
                for k, lft2 in enumerate(nums[i + j + 2:]):

                    three_sum = lft + lft1 + lft2
                    if target - three_sum in track1:
                        res.update(
                            [tuple(sorted([lft, lft1, lft2] + trk)) for trk in track1[target - three_sum]])
                    else:
                        track1[lft2].append([lft2])
        return [list(sol) for sol in res]

        # nums.sort()
        # ans = []
        #
        # def NSum(l, r, target, N, result):
        #     if r - l + 1 < N or target < nums[l] * N or target > nums[r] * N:
        #         return
        #     if N == 2:
        #         while l < r:
        #             s = nums[l] + nums[r]
        #             if s == target:
        #                 ans.append(result + [nums[l], nums[r]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1
        #             elif s < target:
        #                 l += 1
        #             else:
        #                 r -= 1
        #     else:
        #         for i in range(l, r + 1):
        #             if i == l or (i > l and nums[i - 1] != nums[i]):
        #                 NSum(i + 1, r, target - nums[i], N - 1, result + [nums[i]])
        #
        # NSum(0, len(nums) - 1, target, 4, [])
        # return ans

    @classmethod
    def remove_nth_from_list_end(cls, head, n):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None

        counter = 0
        nnode = None
        ptr = head

        while ptr is not None:
            if counter >= n:
                nnode = nnode.next if nnode else head
            counter += 1
            ptr = ptr.next

        if nnode is None:
            head = head.next
            return head

        node_remove = nnode.next
        if node_remove is not None:
            nnode.next = node_remove.next
        else:
            nnode.val = ""

        return head

    @classmethod
    def valid_paranthesis(cls, par):
        """
        #stack
        :param par:
        :return:
        """
        if not par:
            return True
        par_dict = {"[": "]",
                    "{": "}",
                    "(": ")"}
        stack = []
        for c in par:
            if c in par_dict:
                stack.append(c)
            else:
                if len(stack) is not 0 and par_dict[stack[len(stack) - 1]] == c:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

    @classmethod
    def merge_two_sorted_list(cls, l1, l2):

        head = None
        ptr = None

        def append_node(n1):
            nonlocal head
            nonlocal ptr
            if head is None:
                head = ptr = n1
            else:
                ptr.next = n1
                ptr = ptr.next
            return n1.next

        # loop over till one list is exhasted
        while l1 and l2:
            if l1.val < l2.val:
                l1 = append_node(l1)
            elif l1.val > l2.val:
                l2 = append_node(l2)
            else:
                l1 = append_node(l1)
                l2 = append_node(l2)

        # handle residuals
        if l1:
            append_node(l1)
        elif l2:
            append_node(l2)

        return head


if __name__ == "__main__":
    sol = Solution()
    sol.longest_common_prefix(sys.argv[1])
