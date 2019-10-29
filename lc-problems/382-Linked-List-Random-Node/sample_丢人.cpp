/* Definition for singly-linked list.
  * struct ListNode {
    *int       val;
    *ListNode* next;
    *ListNode( int x ) : val( x ), next( NULL ){}*
};
*/
class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution( ListNode* head ) {
        if ( head == nullptr )
            return;
        this->head = head;
    }

    /** Returns a random node's value. */
    int getRandom() {
        ListNode* cur = head;
        int       len = 0;
        while ( cur ) {
            cur = cur->next;
            len++;
        }
        int random_num = 0 + rand() % len;
        int tmp        = random_num;
        cur            = head;
        while ( tmp-- ) {
            cur = cur->next;
        }
        return cur->val;
    }

private:
    ListNode* head;
    int       len;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */