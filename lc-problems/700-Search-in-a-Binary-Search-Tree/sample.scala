/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def searchBST(root: TreeNode, `val`: Int): TreeNode = (root, `val`) match {
        case (null, _) => null
        case (root, `val`) if root.value > `val` => searchBST(root.left, `val`)
        case (root, `val`) if root.value < `val` => searchBST(root.right, `val`)
        case (root, `val`) if root.value == `val` => root
    }
}