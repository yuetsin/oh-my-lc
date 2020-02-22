class Solution {
public:
    string shortestCompletingWord( string licensePlate, vector< string >& words ) {

        // count character in licensePlate
        vector< int > src( 26, 0 );
        for_each( begin( licensePlate ), end( licensePlate ), [&]( char c ) {
            c = tolower( c );
            if ( c >= 'a' && c <= 'z' ) {
                ++src[ c - 'a' ];
            }
        } );

        string result;
        for ( string& word : words ) {
            vector< int > dst( 26, 0 );

            // count each word
            for_each( begin( word ), end( word ), [&]( char c ) { ++dst[ c - 'a' ]; } );

            // use a lambda function here
            bool res = [&]() {
                for ( int i = 0; i < 26; ++i ) {
                    if ( dst[ i ] < src[ i ] )
                        return false;
                }
                return true;
            }();
            if ( res && ( result.empty() || word.size() < result.size() ) ) {
                result = word;
            };
        }

        return result;
    }
};