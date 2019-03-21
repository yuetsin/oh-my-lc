class Solution {
public:
    void appendNode(ListNode* head, int val) {
        ListNode* newNode = new ListNode(val);
        ListNode* temp    = head;
        while (temp) {
            if (temp->next == NULL) {
                temp->next = newNode;
                return;
            }
            temp = temp->next;
        }
    }
    int getResultSumFromValues(int a, int b, int* carry) {
        int result = a + b + *carry;
        if (result >= 10) {
            *carry = result / 10;
            result = result % 10;
        }
        else
            *carry = 0;
        return result;
    }
}