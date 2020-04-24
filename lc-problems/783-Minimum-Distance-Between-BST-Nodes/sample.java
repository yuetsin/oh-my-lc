/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  private int diff;
  private int lastValue;
  public int minDiffInBST(TreeNode root) {
    diff = Integer.MAX_VALUE;
    lastValue = Integer.MAX_VALUE;
    inorder(root);
    return diff;
  }

  private void inorder(TreeNode node) {
    if (node != null) {
      inorder(node.left);
      if (lastValue != Integer.MAX_VALUE) {
        diff = Math.min(diff, node.val - lastValue);
      }

      lastValue = node.val;

      inorder(node.right);
    }
  }
}