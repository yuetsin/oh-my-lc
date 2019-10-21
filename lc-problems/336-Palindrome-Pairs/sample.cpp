vector< vector< int > > palindromepairs_search( vector< string >& words ) {
    unordered_map< string, int > stridx;
    int                          len, i, j, l, r, p;
    string                       subw;
    vector< vector< int > >      ret;

    for ( i = 0; i < words.size(); i++ )
        stridx[ words[ i ] ] = i;

    for ( i = 0; i < words.size(); i++ ) {  // O(n * l^2)
        len = words[ i ].size();

        // iterate all the possible prefix/suffix which can
        // make a panlindrome.
        for ( p = 0; p <= 2 * len; p++ ) {  // O(l^2 )

            // find the longest panlindrome by pivot at p.
            l = p == 0 ? -1 : ( p - 1 ) / 2;
            r = p / 2;
            while ( l >= 0 && r < len && words[ i ][ l ] == words[ i ][ r ] ) {  // O(l)
                l--;
                r++;
            }

            // No candidate exists unless the longest
            // panlindrom reaches one end of word[i]
            if ( l >= 0 && r < len )
                continue;

            // generate the desired prefix/suffix
            if ( l < 0 )
                subw = words[ i ].substr( r, len - r );  // O(l)
            else
                subw = words[ i ].substr( 0, l + 1 );
            reverse( subw.begin(), subw.end() );  // O(l)

            // check if the candidate exists in the words
            if ( stridx.count( subw ) == 0 )  // O(1)
                continue;

            j = stridx[ subw ];

            // avoid duplicate
            // ASSERT(words[i].size() >= words[j].size());
            if ( words[ i ].size() == words[ j ].size() && j <= i )
                continue;

            if ( l < 0 )
                ret.push_back( { j, i } );
            if ( r >= len )
                ret.push_back( { i, j } );
        }
    }

    return ret;
}