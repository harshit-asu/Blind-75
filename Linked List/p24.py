"""

Problem: 23. Merge k Sorted Lists

URL: https://leetcode.com/problems/merge-k-sorted-lists/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because ListNode is implemented here.
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None
    newLists = []
    for i in range(len(lists)):
        if lists[i]:
            newLists.append(lists[i])
    del lists
    lists = newLists
    result = None
    temp = None
    while len(lists):
        minValue = 10**4+1
        minIndex = -1
        for i in range(len(lists)):
            if minValue > lists[i].val:
                minValue = lists[i].val
                minIndex = i
        if result:
            temp.next = ListNode(val=lists[minIndex].val)
            temp = temp.next
        else:
            result = ListNode(val=lists[minIndex].val)
            temp = result
        lists[minIndex] = lists[minIndex].next
        if lists[minIndex] == None:
            del lists[minIndex]
    return result