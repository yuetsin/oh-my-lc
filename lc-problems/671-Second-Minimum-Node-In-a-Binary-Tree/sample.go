// written by @tjucoder

func findSecondMinimumValue(root *TreeNode) int {
    min, sec := root.Val, -1
    currentNodes := []*TreeNode{}
    if root.Left != nil {
        currentNodes = append(currentNodes, root.Left)
    }
    if root.Right != nil {
        currentNodes = append(currentNodes, root.Right)
    }
    for len(currentNodes) != 0 {
        nextNodes := []*TreeNode{}
        for _, node := range currentNodes {
            if sec != -1 && node.Val >= sec {
                continue
            }
            if node.Val > min {
                sec = node.Val
            }
            if node.Left != nil {
                nextNodes = append(nextNodes, node.Left)
            }
            if node.Right != nil {
                nextNodes = append(nextNodes, node.Right)
            }
        }
        currentNodes = nextNodes
    }
    return sec
}