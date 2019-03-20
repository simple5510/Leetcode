'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        return max(dict, key=dict.get)

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]

    # Divide and Conquer
    def majorityElement3(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        # 如果存在，分别计算左半部份和右半部份的众数
        a = self.majorityElement(nums[:len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2:])
        if a == b:
            return a
        # 左右众数不同时，如果count(a)比n/2,则返回a，否则返回b
        return [b, a][nums.count(a) > len(nums) // 2]

    # the idea here is if a pair of elements from the
    # list is not the same, then delete both, the last
    # remaining element is the majority number
    def majorityElement4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0
        for num in nums:
            if not candidate:
                candidate = num
                count = 1
            elif num != candidate:
                count -= 1
                if not count:
                    candidate = None
            else:
                count += 1
        return candidate
