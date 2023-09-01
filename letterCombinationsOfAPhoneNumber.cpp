class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        
        vector<string> combinations = {""};
        vector<string> digitToLetters = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        for (char digit : digits) {
            vector<string> newCombinations;
            string letters = digitToLetters[digit - '0'];
            
            for (string combination : combinations) {
                for (char letter : letters) {
                    newCombinations.push_back(combination + letter);
                }
            }
            
            combinations = move(newCombinations);
        }

        return combinations;
    }
};
