class Solution {
    func findDisappearedNumbers(_ nums: [Int]) -> [Int] {
        if nums.isEmpty {
            return nums
        }
        
        return Array(
            Set(1...nums.count).subtracting(nums)
        )
    }
}