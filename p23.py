"""

Problem: 141. Linked List Cycle

URL: https://leetcode.com/problems/linked-list-cycle/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because ListNode is implemented here.
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False