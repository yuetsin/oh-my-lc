class Solution {
public:
    bool checkInclusion( string s1, string s2 ) {
        // generate char statistics for s1
        unordered_map< char, int > stat;
        for ( char c : s1 ) {
            if ( stat.count( c ) )
                stat[ c ] += 1;
            else
                stat[ c ] = 1;
        }
        // go through s2 with window [i..j]
        unordered_map< char, int > freq;
        for ( auto& p : stat ) {
            freq[ p.first ] = 0;
        }
        int i   = 0;  // window starting pos
        int j   = 0;  // window ending pos
        int cnt = 0;  // total count of chars
        while ( j < s2.size() ) {
            char c = s2[ j ];
            if ( !freq.count( c ) ) {
                // see a char that is not in s1, clear freq
                j += 1;
                i = j;
                for ( auto& p : freq ) {
                    p.second = 0;
                }
                cnt = 0;
            }
            else {
                // see a char that is in s1
                freq[ c ] += 1;
                j += 1;
                cnt += 1;
                while ( freq[ c ] > stat[ c ] ) {
                    freq[ s2[ i ] ] -= 1;
                    cnt -= 1;
                    i += 1;
                }
                if ( cnt == s1.size() )
                    return true;
            }
        }
        return false;
    }
};