class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 0
        while (1 << k) - 1 < n:
            k += 1
        return (1 << k) - 1