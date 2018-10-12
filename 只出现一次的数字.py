# 我的答案
class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]

    # 最快答案
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = nums[0]
        # for i in range(1,len(nums)):
        #     res = res^nums[i]
        # return res
        return sum(set(nums)) * 2 - sum(nums)

    # 新鲜答案
    # 思想：对每个数进行一次运算，如果两个数字相同则会抵消，比如异或运算class Solution:
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res
