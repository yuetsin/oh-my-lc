// written by @dirkbe11

class Solution {
public:
    int maxChunksToSorted( vector< int >& arr ) {
        int chunks      = 0;
        int countingSum = 0;

        for ( int i = 0; i < arr.size(); i++ ) {
            countingSum += arr[ i ];
            if ( ( i * ( i + 1 ) ) / 2 == countingSum )
                chunks++;
        }
        return chunks;
    }
};