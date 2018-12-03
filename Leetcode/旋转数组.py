"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。"""


class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k == 0 or k == l:
            return
        k = k % l
        nums.extend(nums[:l - k])
        del nums[:l - k]

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = k % length
        nums[:] = nums[-i:] + nums[:-i]

    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 or k == 0:
            nums = nums
        elif len(nums) == 2:
            if k % 2 == 1:
                nums.reverse()
        else:
            nums[:] = nums[-k:] + nums[:len(nums) - k]
