"""

Problem: 295. Find Median from Data Stream

URL: https://leetcode.com/problems/find-median-from-data-stream/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

# maintain two heaps
# adjust so that median lies in the boundary
import heapq
class MedianFinder:

    def __init__(self):
        self.lower = list()
        self.higher = list()

    def maxHeapPush(self, val):
        return heapq.heappush(self.lower, -val)
    
    def maxHeapPop(self):
        return -heapq.heappop(self.lower)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.higher, num)
        while self.lower and self.higher:
            a = self.maxHeapPop()
            b = heapq.heappop(self.higher)
            self.maxHeapPush(a)
            if a > b:
                self.maxHeapPush(b)
            else:
                heapq.heappush(self.higher, b)
                break
        while len(self.higher) - len(self.lower) > 1:
            self.maxHeapPush(heapq.heappop(self.higher))
        while len(self.lower) - len(self.higher) > 1:
            a = self.maxHeapPop()
            heapq.heappush(self.higher, a)

    def findMedian(self) -> float:
        lower_len = len(self.lower)
        higher_len = len(self.higher)
        if lower_len == higher_len:
            a = heapq.heappop(self.higher)
            b = self.maxHeapPop()
            heapq.heappush(self.higher, a)
            self.maxHeapPush(b)
            return (a + b)/2
        elif lower_len > higher_len:
            a = self.maxHeapPop()
            self.maxHeapPush(a)
            return float(a)
        else:
            a = heapq.heappop(self.higher)
            heapq.heappush(self.higher, a)
            return float(a)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()