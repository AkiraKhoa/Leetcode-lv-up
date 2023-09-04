class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head; // No need to swap if there are 0 or 1 nodes
        }
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        
        while (head && head->next) {
            ListNode* first = head;
            ListNode* second = head->next;
            
            // Swap the pair of nodes
            prev->next = second;
            first->next = second->next;
            second->next = first;
            
            // Update head and prev for the next pair
            prev = first;
            head = first->next;
        }
        
        return dummy.next;
    }
};
