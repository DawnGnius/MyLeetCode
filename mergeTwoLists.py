# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = head =  ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
            else:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
        if not l1:
            l3.next = l2
        if not l2:
            l3.next = l1
        return head.next


A = Solution()
l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(5)
l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

B = A.mergeTwoLists(l1, l2)
while B:
    print(B.val)
    B = B.next
