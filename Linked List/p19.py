"""

Problem: 206. Reverse Linked List

URL: https://leetcode.com/problems/reverse-linked-list/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

# run this on Leetcode, because ListNode is implemented here.
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return head
    prev = None
    while True:
        temp = head.next
        head.next = prev
        prev = head
        if temp != None:
            head = temp
        else:
            break
    return head