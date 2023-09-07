class Solution {
   public:
   void nextPermutation ( vector<int>& a , int max_right = -1 ) {
      //  LEFT AND RIGHT SUBARRAY BY IMAGINING A SINGLE PARTITION
      for ( int i = a.size ( ) - 1; i >= 1; i-- ) {
         max_right = max ( max_right , a [ i ] );
         if ( a [ i - 1 ] < max_right ) {
            reverse ( a.begin ( ) + i , a.end ( ) );
            // CALCULATING THE NUMBER TO SWAP IN THE RIGHT SUBARRAY 
            int element_to_swap = upper_bound ( a.begin ( ) + i , a.end ( ) , a [ i - 1 ] ) - a.begin ( );
            swap ( a [ element_to_swap ] , a [ i - 1 ] );
            return;
            }
         }
      reverse ( a.begin ( ) , a.end ( ) );
      }
   };