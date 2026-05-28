import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        int[] nums = {-1,0,1,2,-1,-4};
    }
}
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        //枚举a
        for(int i = 0; i < n; i++){
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int l=i+1,r=n-1;
            int target = -nums[i];
            while(l<r){
                int sum = nums[l] + nums[r];
                if(sum == target){
                    ans.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    l++;r--;
                    //跳过重复
                    while(l<r && nums[l] == nums[l-1]) l++;
                    while(l<r && nums[r] == nums[r+1]) r--;
                }else if(sum < target){
                    l++;
                }else {
                    r--;
                }
            }
        }

        return ans;
    }
}
