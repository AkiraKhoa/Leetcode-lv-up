class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        if (n <= 1) {
            return s;
        }

        string t = preProcess(s);
        n = t.length();
        vector<int> p(n, 0);
        int center = 0, right = 0;
        int maxLen = 0, maxCenter = 0;

        for (int i = 1; i < n - 1; ++i) {
            int mirror = 2 * center - i;

            if (i < right) {
                p[i] = min(right - i, p[mirror]);
            }

            // Attempt to expand palindrome centered at i
            while (t[i + p[i] + 1] == t[i - p[i] - 1]) {
                ++p[i];
            }

            // If palindrome centered at i expands past right,
            // adjust center based on palindrome's new right edge
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }

            // Update the longest palindrome if necessary
            if (p[i] > maxLen) {
                maxLen = p[i];
                maxCenter = i;
            }
        }

        int start = (maxCenter - maxLen) / 2;
        return s.substr(start, maxLen);
    }

private:
    string preProcess(const string& s) {
        int n = s.length();
        if (n == 0) {
            return "^$";
        }

        string t = "^";
        for (int i = 0; i < n; ++i) {
            t += "#" + s.substr(i, 1);
        }
        t += "#$";
        return t;
    }
};