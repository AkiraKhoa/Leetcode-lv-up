class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length();
        int n = needle.length();

        if (n == 0) {
            return 0; // An empty needle is always present at the beginning.
        }

        if (n > m) {
            return -1; // Needle cannot be longer than haystack.
        }

        // Compute the KMP prefix table for the needle.
        vector<int> lps(n, 0);
        computeLPS(needle, lps);

        int i = 0; // Index for haystack
        int j = 0; // Index for needle

        while (i < m) {
            if (haystack[i] == needle[j]) {
                ++i;
                ++j;
            }

            if (j == n) {
                return i - j; // Needle found starting at i-j in haystack.
            } else if (i < m && haystack[i] != needle[j]) {
                if (j != 0) {
                    j = lps[j - 1]; // Use the prefix table to backtrack in the needle.
                } else {
                    ++i; // No match, move the haystack index.
                }
            }
        }

        return -1; // Needle is not found in haystack.
    }

private:
    void computeLPS(const string& needle, vector<int>& lps) {
        int len = 0; // Length of the previous longest prefix-suffix

        for (int i = 1; i < needle.length();) {
            if (needle[i] == needle[len]) {
                ++len;
                lps[i] = len;
                ++i;
            } else {
                if (len != 0) {
                    len = lps[len - 1]; // Backtrack using the prefix table.
                } else {
                    lps[i] = 0;
                    ++i;
                }
            }
        }
    }
};
