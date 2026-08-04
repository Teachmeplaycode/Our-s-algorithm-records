//https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	map<int,int> mp;
    	vector<int> ans;
		for(int i = 0;i < nums.size(); i++){
			mp[i] = nums[i];
		}
    }
};
int main(){
    vector<int> nums = {2,7,11,15};
    int target = 9;
    Solution sol = Solution();
    sol.twoSum(nums,target);
    return 0;
}
