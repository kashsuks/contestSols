class Solution:
    def minArraySum(self, nums: list[int], delVal: int, op1: int, op2: int) -> int:
        n = len(nums)
        dp = [[[float('inf')] * (op2 + 1) for _ in range(op1 + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 0

        def checkOp12(x: int, delVal: int) -> bool:
            return (x + 1) // 2 >= delVal

        for i in range(1, n + 1):
            for j in range(min(op1, i) + 1):
                for k in range(min(op2, i) + 1):
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k] + nums[i - 1])
                    
                    if j >= 1:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][k] + (nums[i - 1] + 1) // 2)
                    
                    if k >= 1 and nums[i - 1] >= delVal:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k - 1] + (nums[i - 1] - delVal))
                    
                    if j >= 1 and k >= 1 and checkOp12(nums[i - 1], delVal):
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][k - 1] + (nums[i - 1] + 1) // 2 - delVal)
                    
                    if j >= 1 and k >= 1 and nums[i - 1] >= delVal:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][k - 1] + ((nums[i - 1] - delVal + 1) // 2))

        return min(dp[n][i][j] for i in range(op1 + 1) for j in range(op2 + 1))
