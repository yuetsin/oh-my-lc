class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        Deque<TreeNode> stack = new ArrayDeque<>();
        Deque<StringBuilder> stackStr = new ArrayDeque<>();
        stack.offerFirst(root);
        stackStr.offerFirst(new StringBuilder());
        
        while (!stack.isEmpty()) {
            TreeNode curNode = stack.pollFirst();
            StringBuilder curStr = stackStr.pollFirst();
            
            if (curNode.left == null && curNode.right == null) {
                StringBuilder temp = new StringBuilder(curStr.append(curNode.val));
                res.add(temp.toString());
            }
            curStr.append(curNode.val + "->");
            if (curNode.right != null) {
                stack.offerFirst(curNode.right);
                StringBuilder temp = new StringBuilder(curStr);
                stackStr.offerFirst(temp);    
            }
            if (curNode.left != null) {
                stack.offerFirst(curNode.left);
                StringBuilder temp = new StringBuilder(curStr);
                stackStr.offerFirst(temp);
            }
        }
        return res;
    }
}