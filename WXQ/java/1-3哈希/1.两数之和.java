package hoot100;

import java.util.HashMap;
import java.util.Map;

public class Test {
    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        Solution solution=new Solution();
        int[] result=solution.twoSum(nums,target);
        System.out.println(result[0]+","+result[1]);
    }
}
//暴力枚举
class  Solution{
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[0];
    }
}
//哈希表
class Solution1{
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashtable = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            if (hashtable.containsKey(target-nums[i])){
                return new int[]{hashtable.get(target-nums[i]),i};
            }
            hashtable.put(nums[i], i);
        }
        return new int[0];
    }
}
