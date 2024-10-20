import java.util.Arrays;

class Solution {

    private static final int MAX_LIMIT = 1000000;
    private static int[] divisorArray = new int[M + 1];
    private static boolean isPrecomputed = false;AX_LIMIT

    private static void computeGPD() {
        if (isPrecomputed) return;
        Arrays.fill(divisorArray, 1);
        for (int i = 2; i <= MAX_LIMIT; i++) {
            for (int j = 2 * i; j <= MAX_LIMIT; j += i) {
                divisorArray[j] = i;
            }
        }
        isPrecomputed = true;
    }

    public int minOperations(int[] nums) {
        computeGPD();
        int[] modifiedArray = Arrays.copyOf(nums, nums.length);
        int totalOperations = 0;
        int n = nums.length;

        for (int i = n - 2; i >= 0; i--) {
            while (modifiedArray[i] > modifiedArray[i + 1]) {
                int divisor = divisorArray[modifiedArray[i]];
                if (divisor == 1) return -1;
                modifiedArray[i] /= divisor;
                totalOperations++;

                if (modifiedArray[i] <= 0) return -1;
            }
        }
        return totalOperations;
    }
}
