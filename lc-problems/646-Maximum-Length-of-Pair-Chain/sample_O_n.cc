class Solution {
public:
    int findLongestChain( vector< vector< int > >& pairs ) {
        int n = pairs.size();
        if ( n == 0 )
            return 0;
        vector< int > f( 2001 );
        for ( int i = 0; i < n; i++ ) {
            pairs[ i ][ 0 ] += 1000;
            pairs[ i ][ 1 ] += 1000;
            if ( f[ pairs[ i ][ 0 ] ] == 0 )
                f[ pairs[ i ][ 0 ] ] = pairs[ i ][ 1 ];
            else
                f[ pairs[ i ][ 0 ] ] = min( f[ pairs[ i ][ 0 ] ], pairs[ i ][ 1 ] );
        }
        vector< int > dp( 2001 );
        int           mx = 0;
        for ( int i = 1; i <= 2000; i++ ) {
            if ( f[ i ] )
                dp[ f[ i ] ] = max( dp[ f[ i ] ], mx + 1 );
            mx = max( mx, dp[ i ] );
        }
        return mx;
    }
};