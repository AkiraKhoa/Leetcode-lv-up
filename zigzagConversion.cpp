class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) {
            return s;
        }

        string result;
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; ++i) {
            for (int j = 0; j + i < s.length(); j += cycleLen) {
                result += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < s.length()) {
                    result += s[j + cycleLen - i];
                }
            }
        }

        return result;
    }
};