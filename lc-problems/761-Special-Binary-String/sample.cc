#include <vector>

using std::vector;

class Solution {
public:
    vector< int > end;
    void          findSpecialBinaryString( string& s, int start ) {
        int next = start + 1;
        while ( s[ next ] != '0' ) {
            findSpecialBinaryString( s, next );
            next = end[ next ];
        }
        end[ start ] = next + 1;
    }
    string makeLargestSpecial( string S ) {
        string s;
        end = vector< int >( S.size(), -1 );
        do {
            s = S;
            for ( int i = 0; i < s.size(); ) {
                findSpecialBinaryString( s, i );
                i = end[ i ];
            }
            for ( int i = 0; i < s.size(); i++ )
                if ( s[ i ] == '1' ) {
                    // if SpecialBinaryString [ i, end[i] ) is lexicographically smaller than [ end[i], end[end[i]] ), swap them.
                    if ( s[ end[ i ] ] == '1' && s.substr( i, end[ i ] - i ) < s.substr( end[ i ], end[ end[ i ] ] - end[ i ] ) ) {
                        S = s.substr( 0, i ) + s.substr( end[ i ], end[ end[ i ] ] - end[ i ] ) + s.substr( i, end[ i ] - i ) + s.substr( end[ end[ i ] ], s.size() - end[ end[ i ] ] );
                        break;
                    }
                }
        } while ( s < S );
        return s;
    }
};