
class Solution {
    var minDiff = Int.max
    var last: Int? = nil
    
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }
        getMinimumDifference(node.left)
        if let item = last { minDiff = min(minDiff, abs(node.val - item)) }
        last = node.val
        getMinimumDifference(node.right)
        return minDiff
    }
}