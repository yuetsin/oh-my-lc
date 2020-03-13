// written by @KaziNizamul

class Solution {
public:
    int maxChunksToSorted( vector< int >& a ) {

        long          s1 = 0, s2 = 0, count = 0;
        vector< int > v = a;
        sort( v.begin(), v.end() );

        for ( int i = 0; i < a.size(); i++ ) {
            s1 = s1 + a[ i ];
            s2 = s2 + v[ i ];

            if ( s1 == s2 )
                count++;
        }

        return count;
    }
};