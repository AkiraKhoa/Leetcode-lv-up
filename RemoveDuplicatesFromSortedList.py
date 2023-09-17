class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* current = head;

        while (current && current->next) {
            if (current->val == current->next->val) {
                current->val = current->next->val; // Update the current node's value.
                current->next = current->next->next; // Skip the duplicate.
            } else {
                current = current->next;
            }
        }

        return head;
    }
};
