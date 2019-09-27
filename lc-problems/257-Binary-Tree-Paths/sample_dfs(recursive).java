class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        List<Integer> cur = new ArrayList<>();
        helper(root, cur, res);
        return res;
    }
    
    private void helper(TreeNode root, List<Integer> cur, List<String> res) {
        if (root == null) {
            //res.add(buildString(cur));
            return;
        }
        if (root.left == null && root.right == null) {
            cur.add(root.val);
            res.add(buildString(cur));
            cur.remove(cur.size() - 1);
            return;
        }
        cur.add(root.val);
        helper(root.left, cur, res);
        helper(root.right, cur, res);
        cur.remove(cur.size() - 1);
    }
    
    private String buildString(List<Integer> cur) {
        int size = cur.size();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size - 1; i++) {
            sb.append(cur.get(i));
            sb.append("->");
        }
        sb.append(cur.get(size - 1));
        return sb.toString();
    }
}
