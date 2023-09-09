class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check rows and columns.
        for (int i = 0; i < 9; i++) {
            vector<bool> rowCheck(9, false);
            vector<bool> colCheck(9, false);
            
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int rowDigit = board[i][j] - '1';
                    if (rowCheck[rowDigit]) return false;
                    rowCheck[rowDigit] = true;
                }
                
                if (board[j][i] != '.') {
                    int colDigit = board[j][i] - '1';
                    if (colCheck[colDigit]) return false;
                    colCheck[colDigit] = true;
                }
            }
        }
        
        // Check 3x3 subgrids.
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                vector<bool> subgridCheck(9, false);
                
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        if (board[k][l] != '.') {
                            int subgridDigit = board[k][l] - '1';
                            if (subgridCheck[subgridDigit]) return false;
                            subgridCheck[subgridDigit] = true;
                        }
                    }
                }
            }
        }
        
        return true;
    }
};