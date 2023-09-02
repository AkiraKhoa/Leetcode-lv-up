class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) {
            return n; // No duplicates or empty array
        }

        int slow = 1; // Slow pointer (points to the next non-duplicate position)

        for (int fast = 1; fast < n; ++fast) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                ++slow;
            }
        }

        return slow; // Length of the modified array without duplicates
    }
};
