''''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums: return []
        # window存的下标，res存的输出结果
        window, res = [], []
        for i, x in enumerate(nums):
            #  判断最左的元素是否超出window范围,如果超出范围则移除，其中i-k是最左边的元素下标
            if i >= k and window[0] <= i - k:
                window.pop(0)
            # 对新进入window的元素x进行判断：只要x比原有最大的元素还大，就可以移除原有的元素只保留x
            while window and nums[window[-1]] <= x:
                window.pop()
            # 下标存入window
            window.append(i)
            # 从第k+1个数开始，把每次滑动的最大值，也就是窗内最大值放到res
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

    # 原理相同使用内置dequeue
    def maxSlidingWindow2(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out
