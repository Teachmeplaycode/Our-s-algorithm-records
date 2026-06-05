import java.util.*;

public class Test3 {
    public static void main(String[] args) {
        int[] nums={1};
        int k = 0;
        Solution solution = new Solution();
        int result=solution.subarraySum(nums,k);
        System.out.println(result);
    }
}
class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        int prefixSum=0,count=0;
        map.put(0,1);
        for (int num : nums) {
            prefixSum += num;
            int need = prefixSum - k;
            count += map.getOrDefault(need, 0);
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }
}

