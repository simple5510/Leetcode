''''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        has_no_or_one_node = (not head or not head.next)
        if has_no_or_one_node or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                begin = self._reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummy.next

    def _reverse(self, begin, end):
        prev, curr, first = begin, begin.next, begin.next
        while curr != end:
            curr.next, prev, curr = prev, curr, curr.next
        begin.next, first.next = prev, curr
        return first

    def reverseKGroup2(self, head, k):  # reverse node can happen in scan process.
        length = 0
        dummy = ListNode(0)  # use to point to head
        dummy.next = head
        t = head
        while t:
            length += 1
            t = t.next
        first = None
        prev_last = dummy
        curr = head  # mark first node to point to next first.
        first = head  # mark node like 1,it is start of origin linked list
        for _ in range(length / k):  # 1 2 3 -> prev_last-> 3 2 1->curr mark 1 and prev_last to link two part
            last = None  # at first first's next is still unknown,mark as None.
            for _ in range(k):
                tmp = curr.next
                curr.next = last
                last = curr
                curr = tmp
            prev_last.next = last  #
            first.next = curr
            prev_last = first
            first = curr
        return dummy.next
