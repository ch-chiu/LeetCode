# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # tmp_lower = []
        # tmp_higher = []
        # while(head is not None):
        #     if head.val < x:
        #         tmp_lower.append(head.val)
        #     else:
        #         tmp_higher.append(head.val)
        #     head = head.next
        # return tmp_lower + tmp_higher
        tmp1 = l1 = ListNode(None)
        tmp2 = l2 = ListNode(None)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = tmp2.next
        return tmp1.next





