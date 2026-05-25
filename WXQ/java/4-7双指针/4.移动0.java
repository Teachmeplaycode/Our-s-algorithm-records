import java.util.Arrays;

public class Test3 {
    public static void main(String[] args) {
        int[] nums={0,4,0,1,3,2};
        Solution solution=new Solution();
        solution.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
class Solution {
    public void moveZeroes(int[] nums) {
        int n=nums.length,left=0,right=0;
        int temp;
        while(right<n){
            if(nums[right]!=0){
                temp=nums[left];
                nums[left]=nums[right];
                nums[right]=temp;
                left++;
            }
            right++;
        }
    }
}

