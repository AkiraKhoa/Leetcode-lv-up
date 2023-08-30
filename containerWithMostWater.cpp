class Solution {
public:
    int maxArea(vector<int>& height) {
        // If you want to improve this code, just do it, and also post it in comments.
        int i = 0, j = height.size()-1;

        int ans = INT_MIN;

        while(i<j) {
            int diff = j-i;

            int a = height[i]; // starting pillar height
            int b = height[j]; // ending pillar height

            int mini = min(a, b); // finding minimum height

            int cur = diff*mini; // CurAns is the diff*mini

            ans = max(ans, cur); // maintaining the maximum

            if(a == b) { // if both pillars height are equal
                ++i, --j;
            }
            else if(a < b) { // if starting pillar is shorter.
                ++i;
            }
            else --j; // if ending pillar is shorter.
        }

        return ans; 
    }
};