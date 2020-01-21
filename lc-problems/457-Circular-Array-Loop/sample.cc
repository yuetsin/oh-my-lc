class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        for(int i = 0; i < nums.size(); ++i) {
            if(circularArrayLoop(nums, i)) {
                return true;
            }
        }
        return false;
    }
    
    bool circularArrayLoop(vector<int>& nums, int i) {
        if(0 == nums[i]) {
            return false;
        }
        
        if(abs(nums[i]) > 5000) {
            return true;
        }
        
        int next_step = nums[i];
        
        int next_i = (nums.size() + i + next_step) % nums.size();
        
        if(i == next_i || (next_step > 0 && nums[next_i] < 0) || (next_step < 0 && nums[next_i] > 0)) {
            nums[i] = 0;
            return false;
        }   
         
        nums[i] *= 10000;
        
        bool ret = circularArrayLoop(nums, next_i);
        
        nums[i] = 0;
        
        return ret;
    } 
};