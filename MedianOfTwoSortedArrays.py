class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        
        // Ensure nums1 is the smaller array for simplicity.
        if (m > n) {
            swap(nums1, nums2);
            swap(m, n);
        }
        
        int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
        
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            
            if (i < m && nums2[j - 1] > nums1[i]) {
                // Increase i to make the left part of the merged array larger.
                iMin = i + 1;
            } else if (i > 0 && nums1[i - 1] > nums2[j]) {
                // Decrease i to make the left part of the merged array smaller.
                iMax = i - 1;
            } else {
                // Found the correct partition.
                int maxOfLeft, minOfRight;
                if (i == 0) maxOfLeft = nums2[j - 1];
                else if (j == 0) maxOfLeft = nums1[i - 1];
                else maxOfLeft = max(nums1[i - 1], nums2[j - 1]);
                
                if ((m + n) % 2 == 1) return maxOfLeft;
                
                if (i == m) minOfRight = nums2[j];
                else if (j == n) minOfRight = nums1[i];
                else minOfRight = min(nums1[i], nums2[j]);
                
                return (maxOfLeft + minOfRight) / 2.0;
            }
        }
        
        // If reach here, it means the input arrays are not sorted. Handle this as needed.
        return 0.0;
    }
};
