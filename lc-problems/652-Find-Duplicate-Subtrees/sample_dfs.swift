class Solution {
    func findDuplicateSubtrees(_ root: TreeNode?) -> [TreeNode?] {
        var res:[TreeNode?] = []
        var map:[String:Int] = [:]
        helper(root, &res, &map)
        return res
    }
    
    func helper(_ root: TreeNode?, _ res: inout [TreeNode?], _ map: inout [String:Int]) -> String {
        guard let node = root else { return "#" }
        let text = node.val.description + "," + helper(node.left, &res, &map) + "," + helper(node.right, &res, &map)
        if map[text] == nil{
            map[text] = 1
        }else{
            if map[text] == 1{
                res.append(node)
                map[text]! += 1
            }
        }
        return text
    }
}