class Solution {
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int validCount = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                if (isValid(nums.clone(), i, true)) validCount++;
                if (isValid(nums.clone(), i, false)) validCount++;
            }
        }

        return validCount;
    }

    private boolean isValid(int[] nums, int start, boolean moveRight) {
        int curr = start;
        int n = nums.length;
        int direction = moveRight ? 1 : -1;

        while (curr >= 0 && curr < n) {
            if (nums[curr] == 0) {
                curr += direction;
            } else {
                nums[curr]--;
                direction *= -1;
                curr += direction;
            }
        }

        for (int num : nums) {
            if (num != 0) return false;
        }

        return true;
    }
}