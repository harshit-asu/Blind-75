"""

Problem: 19. Remove Nth Node From End of List

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because ListNode is implemented here.
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    totalNodes = 0
    temp = head
    while temp:
        temp = temp.next
        totalNodes += 1
    if totalNodes == n:
        return head.next
    currCount = 0
    temp = head
    while True:
        currCount += 1
        if totalNodes - currCount == n:
            temp.next = temp.next.next
            break
        temp = temp.next
    return head