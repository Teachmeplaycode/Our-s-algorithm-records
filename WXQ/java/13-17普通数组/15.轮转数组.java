import java.util.*;

import static java.util.Collections.reverse;

public class Test3 {
    public static void main(String[] args) {
        int[] nums={1,2,3,4,5,6,7};
        int k=3;
        Solution solution = new Solution();
        solution.rotate(nums,k);
    }
}
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k=k%n;
        reverse(nums,0,n-1);//整体翻转
        reverse(nums,0,k-1);//翻转前K个
        reverse(nums,k,n-1);//翻转后K个

    }
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}

