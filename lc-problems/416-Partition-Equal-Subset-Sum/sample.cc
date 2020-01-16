#include <algorithm>
class Solution {
public:
    bool dfs( vector< int >& nums, int i, int acc, int t ) {
        if ( acc == t )
            return true;
        if ( acc > t || i < 0 )
            return false;
        return dfs( nums, i - 1, acc + nums[ i ], t ) || dfs( nums, i - 1, acc, t );
    }
    bool canPartition( vector< int >& nums ) {
        int sum = 0;
        for ( auto n : nums )
            sum += n;
        if ( sum % 2 )
            return false;
        sort( nums.begin(), nums.end() );
        int size = nums.size();
        return dfs( nums, size - 2, nums[ size - 1 ], sum / 2 );
    }
};