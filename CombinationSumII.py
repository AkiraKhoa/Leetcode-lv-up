class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        sort(candidates.begin(), candidates.end()); // Sort candidates to handle duplicates.

        backtrack(candidates, target, 0, current, result);

        return result;
    }

    void backtrack(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue; // Skip duplicates to avoid duplicate combinations.
            }

            current.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], i + 1, current, result); // Use i+1 to avoid reusing the same element.
            current.pop_back();
        }
    }
};
