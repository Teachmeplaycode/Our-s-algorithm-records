import java.util.Arrays;

public class Test3 {
    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        Solution solution = new Solution();
        int result = solution.maxArea(height);
        System.out.println(result);
    }
}
class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int sum=0;
        while (left<right){
            int area=Math.min(height[left],height[right])*(right-left);
            sum=Math.max(sum,area);
            if(height[left]<height[right]){
                ++left;
            }
            else {
                --right;
            }
        }
        return sum;
    }
}

