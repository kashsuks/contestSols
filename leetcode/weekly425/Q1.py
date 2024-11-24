from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSum = float('inf')
        found = False
        
        for size in range(l, r + 1):
            windowSum = sum(nums[:size])
            if windowSum > 0:
                minSum = min(minSum, windowSum)
                found = True
            
            for i in range(size, n):
                windowSum += nums[i] - nums[i - size]
                if windowSum > 0:
                    minSum = min(minSum, windowSum)
                    found = True
        
        return minSum if found else -1