// written by @Colix

func longestUnivaluePath(root *TreeNode) (res int) {
	if root == nil {
		return
	}
	helper(root, root.Val, &res)
	return
}

func helper(node *TreeNode, val int, res *int) int {
	if node == nil {
		return 0
	}
	left, right := helper(node.Left, node.Val, res), helper(node.Right, node.Val, res)
	*res = int(math.Max(float64(*res), float64(left+right)))
	if node.Val == val {
		return 1 + int(math.Max(float64(left), float64(right)))
	}
	return 0
}