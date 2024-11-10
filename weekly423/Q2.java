class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        if (nums == null || nums.size() < 2) return 0;
        int n = nums.size();
        
        int[] leftLength = new int[n];
        leftLength[0] = 1;
        for (int i = 1; i < n; i++) {
            leftLength[i] = nums.get(i) > nums.get(i-1) ? leftLength[i-1] + 1 : 1;
        }
        
        int[] rightLength = new int[n];
        rightLength[n-1] = 1;
        for (int i = n-2; i >= 0; i--) {
            rightLength[i] = nums.get(i) < nums.get(i+1) ? rightLength[i+1] + 1 : 1;
        }
        
        int maxK = 0;
        for (int i = 0; i < n-1; i++) {
            int k = Math.min(leftLength[i], rightLength[i+1]);
            if (i + k < n && k > maxK) {
                maxK = k;
            }
        }
        
        return maxK;
    }
}