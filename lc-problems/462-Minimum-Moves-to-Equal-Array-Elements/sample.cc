// on what basis would you increment the min or increment the max
// you would increment the min if the number of elements equal to the min is greater than the number
// of elements equal to the max
// so we can have a L and R pointer. L = 0, R = size()-1
// and we can continue until L < R is not true
// this will take O(nlogn) time and O(1) space as the time complexity is dominated by sorting 

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int L = 0, R = nums.size()-1, res = 0;
        while (L < R){
            while (L < R && nums[L+1] == nums[L]){
                L++;
            }
            
            while (L < R && nums[R-1] == nums[R]){
                R--;
            }
            
            if (L > nums.size()-1-R){
                res += (nums[R] - nums[R-1]) * (nums.size() - R);
                R--;
            }
            else {
                res += (nums[L+1] - nums[L]) * (L + 1);
                L++;
            }
        }
        
        return res;
    }
};