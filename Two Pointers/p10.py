"""

Problem: 15. 3Sum

URL: https://leetcode.com/problems/3sum/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def threeSum(nums):
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        if nums[0] > 0:
            return []
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = -1*(nums[i]+nums[j])
                if k <= nums[i]:
                    temp = [k, nums[i], nums[j]]
                elif k >= nums[j]:
                    temp = [nums[i], nums[j], k]
                else:
                    temp = [nums[i], k, nums[j]]
                if k in d:
                    if k == nums[i] and k == nums[j] and d[k] > 2:
                        res.add(tuple(temp))
                    elif (k != nums[i] or k != nums[j]) and d[k] > 1:
                        res.add(tuple(temp))
                    elif k != nums[i] and k != nums[j]:
                        res.add(tuple(temp))
        return list(res)


# sample test cases
cases = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0]
]

for case in cases:
    print(case, ":", threeSum(case))