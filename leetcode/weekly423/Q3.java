class Solution {
    public int sumOfGoodSubsequences(int[] nums) {
        int mod = 1_000_000_007; //10^9 +7
        int maxVal = 100_001;

        long[] count = new long[maxVal + 2];
        long[] sum = new long[maxVal + 2];
        long result = 0;

        for (int num : nums) {
            long leftCount = (num > 0) ? count[num - 1] : 0;
            long rightCount = (num < maxVal) ? count[num + 1] : 0;

            long leftSum = (num > 0) ? sum[num - 1] : 0;
            long rightSum = (num < maxVal) ? sum[num + 1] : 0;

            long newCount = (1 + leftCount + rightCount) % mod;

            long part1 = num % mod;
            long part2 = leftSum;
            long part3 = (leftCount * (long) num) % mod;
            long part4 = rightSum;
            long part5 = (rightCount * (long) num) % mod;

            long newSum = (part1 + part2 + part3 + part4 + part5) % mod;

            sum[num] = (sum[num] + newSum) % mod;
            count[num] = (count[num] + newCount) % mod;
            result = (result + newSum) % mod;
        }

        return (int) result;
    }
}
