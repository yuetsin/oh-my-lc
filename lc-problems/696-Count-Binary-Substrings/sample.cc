class Solution {
public:
    int countBinarySubstrings( string s ) {
        int r = 0;
        for ( int p( 1 ), m( 1 ), n( 0 ); p - 1 < size( s ); r += min( n, m ), n = exchange( m, 1 ), p++ )
            for ( ; p < s.size() && s[ p - 1 ] == s[ p ]; p++, m++ )
                ;
        return r;
    }
};