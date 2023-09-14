class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int carry = 1; // Start with a carry of 1.

        for (int i = n - 1; i >= 0 && carry > 0; i--) {
            int sum = digits[i] + carry;
            digits[i] = sum % 10; // Update the current digit.
            carry = sum / 10;    // Update the carry.
        }

        // If there's still a carry, add a new digit at the beginning.
        if (carry > 0) {
            digits.insert(digits.begin(), carry);
        }

        return digits;
    }
};
