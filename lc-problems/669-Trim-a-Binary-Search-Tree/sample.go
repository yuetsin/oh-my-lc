/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // written by @tjucoder
 
 func trimBST(root *TreeNode, L int, R int) *TreeNode {
    return walk(root, L, R)
}

func walk(node *TreeNode, L, R int) *TreeNode {
    if node == nil {
        return nil
    }
    if node.Val < L {
        return walk(node.Right, L, R)
    } else if node.Val > R {
        return walk(node.Left, L, R)
    } else {
        node.Left = walk(node.Left, L, R)
        node.Right = walk(node.Right, L, R)
        return node
    }
}