# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Add the numbers with length of len(l1), and then judge if add a new ListNode is necessary owning to AC(Add Carry)
        flag_ac = 0
        l11 = l1
        l22 = l2
        #How to deal with the first node? Head should link to the first Node.
        tmp = l11.val + l22.val
        if tmp > 9:
            tmp = tmp - 10
            flag_ac = 1
        l3 = ListNode(tmp)
        head = l3
        l11 = l11.next
        l22 = l22.next
        while l11 or l22:
            if l11 and l22:
                tmp = l11.val + l22.val + flag_ac
                flag_ac = 0
                if tmp > 9:
                    tmp = tmp - 10
                    flag_ac = 1
                l3.next = ListNode(tmp)
                l3 = l3.next
                l11 = l11.next
                l22 = l22.next
            elif l11 == None:
                tmp = l22.val + flag_ac
                flag_ac = 0
                if tmp > 9:
                    tmp = tmp - 10
                    flag_ac = 1
                l3.next = ListNode(tmp)
                l3 = l3.next
                l22 = l22.next
            else:
                tmp = l11.val + flag_ac
                flag_ac = 0
                if tmp > 9:
                    tmp = tmp - 10
                    flag_ac = 1
                l3.next = ListNode(tmp)
                l3 = l3.next
                l11 = l11.next
        if flag_ac == 1:#AC, create a new node for l3
            l3.next = ListNode(1)
        return head

## Test
l1 = ListNode(1)
l1.next = ListNode(8)
l2 = ListNode(0)
A = Solution()
re = A.addTwoNumbers(l1,l2)
point = re
while point:
    print(point.val)
    point = point.next