class Solution {
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {
        insert(root, `val`)
        return root
    }
    
    fun insert(root: TreeNode?, `val`: Int) {
        
        if (root == null) return
        if (`val` < root.`val`) {
            if (root.left == null) root.left = TreeNode(`val`)
            else insert(root.left,`val`)
        }
        if (`val` > root.`val`) {
            if (root?.right == null) root.right = TreeNode(`val`)
            else insert(root.right,`val`)
        }
        return
    }
}