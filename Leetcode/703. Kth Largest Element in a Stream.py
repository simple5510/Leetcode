''''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
'''

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.vals = nums
        self.k = k

        # turns vals list into heap
        heapq.heapify(self.vals)
        # vals is now heap

        # only keep k largest elements
        while len(self.vals) > k:
            # remove smallest element from heap
            heapq.heappop(self.vals)

    def add(self, val):

        # if heap size is less than k, simply add element
        if len(self.vals) < self.k:
            heapq.heappush(self.vals, val)
        # if val is greater than min, we need to replace min with val
        elif val > self.vals[0]:
            heapq.heapreplace(self.vals, val)

        # return min
        return self.vals[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
