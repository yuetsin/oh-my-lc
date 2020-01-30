class Solution {
public:
    int findMinMoves( vector< int >& machines ) {
        int total = accumulate( machines.begin(), machines.end(), 0 );
        if ( total % machines.size() != 0 )
            return -1;
        int target = total / machines.size();
        int over   = 0;
        int res    = 0;
        for ( auto m : machines ) {
            over = over + m - target;
            res  = max( res, max( abs( over ), m - target ) );
        }
        return res;
    }
};