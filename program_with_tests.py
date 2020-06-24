"""
Squeezed list

Given a list of integers nums, squeeze from both the left and the right
of nums until there is one remaining element. Return the states at each step.

For example, given [1, 2, 3, 4, 5, 6], return these lists:
[[1, 2, 3, 4, 5, 6],
 [3, 3, 4, 11],
 [6, 15],
 [21]]

Example 1
Input
nums = [1, 2, 3, 4, 5, 6]

Output
[[1, 2, 3, 4, 5, 6],
[3, 3, 4, 11],
[6, 15],
[21]]

Example 2
Input
nums = [1, 2, 3, 4, 5]

Output
[[1, 2, 3, 4, 5],
[3, 3, 9],
[15]]
"""


import unittest


def squeezed_list(nums):
    """
    Implement this function and return thesqueezed list.
    """

    re = []
    re.append(nums)
    for i in range(0, len(nums) // 2):
        if len(nums) == 2:
            val = nums[0]+nums[1]
            l = [val]
            re.append(l)
        else:
            nums[1] = nums[0] + nums[1]
            nums[-2] = nums[-2] + nums[-1]
            nums = nums[1:-1]
            re.append(nums)
    return re


# DO NOT TOUCH THE BELOW CODE
class TestSqueezedList(unittest.TestCase):

    def test_01(self):
        input_nums = [1, 2, 3, 4, 5, 6]
        output_nums = [[1, 2, 3, 4, 5, 6], [3, 3, 4, 11], [6, 15], [21]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

    def test_02(self):
        input_nums = [1, 2, 3, 4, 5]
        output_nums = [[1, 2, 3, 4, 5], [3, 3, 9], [15]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

    def test_03(self):
        input_nums = [5]
        output_nums = [[5]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

    def test_04(self):
        input_nums = [3, 5]
        output_nums = [[3, 5], [8]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

    def test_05(self):
        input_nums = [3, 5, 10]
        output_nums = [[3, 5, 10], [18]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

    def test_06(self):
        input_nums = [1, 2, 3, 4, 3, 4, 3, 4, 5, 3,
                      3, 9, 15, 5, 3, 3, 9, 15, 5, 3, 3, 9, 15]
        output_nums = [[3, 5, 10], [18]]

        self.assertEqual(squeezed_list(input_nums), output_nums)

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs


if __name__ == '__main__':
    unittest.main(verbosity=2)
