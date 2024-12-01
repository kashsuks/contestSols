class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(nums)

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        result = float('-inf')

        for num in nums:
            remaining = total - num

            if remaining % 2 == 0:
                target = remaining // 2
                if target in counts:
                    if counts[target] > 1 or (target != num and counts[target] > 0):
                        result = max(result, num)

        return result