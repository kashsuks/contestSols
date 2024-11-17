class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;
        int left = 0;
        int right = m;
        int answer = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canZeroArray(nums, queries, mid, n)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }

    private boolean canZeroArray(int[] nums, int[][] queries, int k, int n) {
        if (k == 0) {
            for (int num : nums) {
                if (num != 0) return false;
            }
            return true;
        }

        int[] diff = new int[n + 1];
        
        for (int i = 0; i < k; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int val = queries[i][2];
            diff[l] += val;
            if (r + 1 < n) {
                diff[r + 1] -= val;
            }
        }

        int current = 0;
        for (int j = 0; j < n; j++) {
            current += diff[j];
            if (current < nums[j]) {
                return false;
            }
        }

        return true;
    }
}