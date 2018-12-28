''''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        解题思路在于推导出x+k = y, 
        x is the distance before getting in the cycle. y is the distance of the cycle. 
        k is the distance from between the beginning of the cycle to the position two pointers meet first time.
        In this problem, we also assign two pointers: a slow pointer and a fast pointer. 
        The slower one increment one step for each time; on the other hand, the faster one increment two steps for each time.
        For iterating t times, the total steps for each pointers is:
        t = x + my + k
        2t = x + ny + k
        and m, n is how many loops for each pointer iterates
        Next, put these equation together to eliminate t:
        2x + 2my + 2k = x + ny + k
        =>
        x + k = (n - 2m)y
        From the last equation, we can see x + k equals the distance of the cycle, which means after finding the k, we assign the faster pointer to head and also a pointer with one step increment. 
        Next we iterate these two pointers until they meet each other again, and the position is the beginning of the cycle.
        '''
        if not head:
            return None
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
