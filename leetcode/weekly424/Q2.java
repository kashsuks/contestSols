class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int[] decrementCount = new int[nums.length + 1];
        
        for (int[] query : queries) {
            int left = query[0];
            int right = query[1];
            decrementCount[left]++;
            decrementCount[right + 1]--;
        }
        
        for (int i = 1; i < decrementCount.length; i++) {
            decrementCount[i] += decrementCount[i - 1];
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (decrementCount[i] < nums[i]) {
                return false;
            }
        }
        
        return true;
    }
 }