class Solution {
    TreeNode *wrong_node0 = nullptr, *wrong_node1 = nullptr, *prev = nullptr;
    void      verify(TreeNode* cur) {
        if (prev != nullptr && prev->val > cur->val) {
            if (wrong_node0 == nullptr) {
                wrong_node0 = prev;
                wrong_node1 = cur;  // in case the tree has only 2 elements.
            }
            else
                wrong_node1 = cur;
        }
        prev = cur;
    }
    void morrisInorder(TreeNode* root) {
        TreeNode* cur = root;
        while (cur) {
            if (cur->left == nullptr) {
                verify(cur);
                cur = cur->right;
                continue;
            }
            TreeNode* pred = cur->left;
            while (pred->right != nullptr && pred->right != cur)
                pred = pred->right;  // finding predecessor
            if (pred->right == nullptr) {
                pred->right = cur;
                cur         = cur->left;
            }
            else {  // pred -> right == cur;
                pred->right = nullptr;
                verify(cur);
                cur = cur->right;
            }
        }
    }

public:
    void recoverTree(TreeNode* root) {
        morrisInorder(root);
        swap(wrong_node0->val, wrong_node1->val);
    }
};