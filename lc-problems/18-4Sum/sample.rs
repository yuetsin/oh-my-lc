// based on sorted 2sum, with prunes about max2sum, min2sum
impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res = vec![];
        if nums.len() < 4 {
            return res;
        }
        nums.sort();
        
        for i in 0..nums.len()-3{
            // dedup i
            if i > 0 && nums[i] == nums[i-1] { continue; }
            
            for j in i+1..nums.len()-2 {
                // dedup j
                if j > i+1 && nums[j] == nums[j-1] { continue; }
                
                let t2 = target - nums[i] - nums[j];
                let (mut lo, mut hi) = (j+1, nums.len()-1);
                // prune max2sum, min2sum, without prune runtime is 8ms
                let min2sum = nums[lo] + nums[lo+1];
                let max2sum = nums[hi] + nums[hi-1];
                if min2sum > t2 || max2sum < t2 { continue; }
                
                while lo < hi {
                    // dedup lo, hi
                    if lo > j+1 && nums[lo] == nums[lo-1] { lo += 1; continue;}
                    if hi < nums.len() - 1 && nums[hi] == nums[hi+1] { hi -= 1; continue; }
                    
                    let sum = nums[lo] + nums[hi];
                    if sum < t2 {
                        lo += 1;
                    } else if sum > t2 {
                        hi -= 1;
                    } else {
                        res.push(vec![nums[i], nums[j], nums[lo], nums[hi]]);
                        lo += 1;
                        hi -= 1;
                    }
                }
            }
        }
        
        res
    }
}