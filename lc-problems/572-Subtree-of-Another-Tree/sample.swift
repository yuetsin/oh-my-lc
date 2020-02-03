class Solution {
    func isSubtree(_ s: TreeNode?, _ t: TreeNode?) -> Bool {
        if s == nil { return false}
        return isSame(s, t) || isSubtree(s?.left, t) || isSubtree(s?.right, t)
    }
    
    func isSame(_ s: TreeNode?, _ t: TreeNode?) -> Bool {
        if s == nil && t == nil { return true}
        if s == nil || t == nil { return false}
        return ((s?.val == t?.val) && isSame(s?.left, t?.left) && isSame(s?.right, t?.right))
    }
}