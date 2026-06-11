import java.util.*;

public class Test3 {
    public static void main(String[] args) {
        int[] nums={-2,1,-3,4,-1,2,1,-5,4};
        Solution solution = new Solution();
        int result = solution.maxSubArray(nums);
        System.out.println(result);
    }
}
class Solution {
    public int maxSubArray(int[] nums) {
        int pre=0;
        int res=nums[0];
        for(int num:nums){
            pre=Math.max(pre+num,num);
            res=Math.max(res,pre);
        }
        return res;
    }
}

