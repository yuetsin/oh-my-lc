class Solution {
    func tree2str(_ t: TreeNode?) -> String{
        guard let node = t else { return ""}
        var text = node.val.description
        if node.left != nil {
            text += "(" + tree2str(node.left) + ")"
        }
        if node.right != nil{
            if node.left == nil {
                text += "()"
            }
            text += "(" + tree2str(node.right) + ")"
        }
        return text
    }
}