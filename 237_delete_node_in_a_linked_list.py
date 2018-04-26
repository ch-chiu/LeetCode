# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    element_list = [1, 2, 3, 4]
    dummy = cur = ListNode(0)
    for element in element_list:
        cur.next = ListNode(element)
        cur = cur.next
    solution = Solution()
    result = solution.deleteNode(dummy.next.next.next)
    if result:
        print("void Do not return anything, modify node in-place instead.")
    result = dummy.next
    print("For debugging")
