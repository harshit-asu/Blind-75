"""

Problem: 143. Reorder List

URL: https://leetcode.com/problems/reorder-list/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because ListNode is implemented here.
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    queue = []
    stack = []
    count = 0
    while head:
        queue.append(head)
        stack.append(head)
        count += 1
        head = head.next
    q = 1
    s = -1
    head = queue[0]
    count -= 1
    temp = head
    while count:
        temp.next = stack[s]
        temp = temp.next
        s -= 1
        count -= 1
        if count == 0:
            break
        temp.next = queue[q]
        temp = temp.next
        q += 1
        count -= 1
    temp.next = None
    return head