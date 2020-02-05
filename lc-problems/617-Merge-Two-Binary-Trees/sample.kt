
class Solution {
    fun mergeTrees(t1: TreeNode?, t2: TreeNode?): TreeNode? {
        var t3 : TreeNode? = null
        val a = t1?.let{ it.`val`} ?: 0
        val b = t2?.let{ it.`val`} ?: 0
        if(t1 != null || t2 != null) {
            t3 = TreeNode(a + b)
            t3.left = mergeTrees(t1?.left, t2?.left)
            t3.right = mergeTrees(t1?.right, t2?.right)
        }
        return t3
    }
}