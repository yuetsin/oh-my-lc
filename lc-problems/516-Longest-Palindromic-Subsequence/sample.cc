class Solution {
public:
    int longestPalindromeSubseq( string str1 ) {
        // This problem can be treated like the longest common subsequence only if
        // we reverse the given string and treat it as another string and find the
        // longest common subsequence between the two
        string str2 = str1;
        reverse( str1.begin(), str1.end() );
        int                     rows = str2.size() + 1, cols = str1.size() + 1;
        vector< vector< int > > matrix( rows, vector< int >( cols ) );
        fillMatrix( str1, str2, matrix );
        return matrix[ rows - 1 ][ cols - 1 ];
    }

private:
    void fillMatrix( string str1, string str2, vector< vector< int > >& matrix ) {
        for ( int i = 0; i < matrix.size(); i++ ) {
            for ( int j = 0; j < matrix[ i ].size(); j++ ) {
                if ( i == 0 || j == 0 )
                    matrix[ i ][ j ] = 0;
                else if ( str1[ j - 1 ] == str2[ i - 1 ] )
                    matrix[ i ][ j ] = 1 + matrix[ i - 1 ][ j - 1 ];
                else
                    matrix[ i ][ j ] = max( matrix[ i - 1 ][ j ], matrix[ i ][ j - 1 ] );
            }
        }
    }
};