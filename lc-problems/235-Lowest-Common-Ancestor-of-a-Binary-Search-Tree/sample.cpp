/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor( TreeNode* root, TreeNode* p, TreeNode* q ) {
        TreeNode* pointer = root;
        while ( true ) {
            if ( p->val > pointer->val && q->val > pointer->val )
                pointer = pointer->right;
            else if ( p->val < pointer->val && q->val < pointer->val )
                pointer = pointer->left;
            else
                return pointer;
        }
    }
};