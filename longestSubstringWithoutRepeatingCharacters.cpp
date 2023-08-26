class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        vector<int> charIndex(256, -1);  // To store the index of each character's last occurrence
        int maxLength = 0;
        int start = 0;

        for (int i = 0; i < n; ++i) {
            if (charIndex[s[i]] >= start) {
                start = charIndex[s[i]] + 1;
            }
            charIndex[s[i]] = i;
            maxLength = max(maxLength, i - start + 1);
        }

        return maxLength;
    }
};
