class Solution {
    var sum = 0
    func findTilt(_ root: TreeNode?) -> Int {
        helper(root)
        return sum
    }
    
    func helper(_ root: TreeNode?) -> Int{
        guard let node = root else { return 0 }
        let left = helper(node.left)
        let right = helper(node.right)
        sum += abs(left - right)
        return left + right + node.val
    }
}