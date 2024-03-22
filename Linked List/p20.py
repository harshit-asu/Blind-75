"""

Problem: 21. Merge Two Sorted Lists

URL: https://leetcode.com/problems/merge-two-sorted-lists/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because ListNode is implemented here.
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = None
    head = None
    while list1 != None and list2 != None:
        temp = ListNode()
        if list1.val >= list2.val:
            temp.val = list2.val
            list2 = list2.next
        elif list1.val < list2.val:
            temp.val = list1.val
            list1 = list1.next
        if result == None:
            result = temp
            head = temp
        else:
            result.next = temp
            result = result.next
    if head == None:
        if list1 != None:
            return list1
        else:
            return list2
    else:
        if list1 != None:
            result.next = list1
        else:
            result.next = list2
    return head