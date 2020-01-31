bool Solution::cmp( string& s1, string& s2 ) {
    if ( s1.size() < s2.size() )
        return true;
    else if ( s1.size() == s2.size() ) {
        if ( s1 > s2 )
            return true;
    }
    return false;
}

string Solution::findLongestWord( string s, vector< string >& d ) {
    if ( s.size() == 0 || d.size() == 0 )
        return string();
    int    i, j;
    string ans;
    for ( auto it = d.begin(); it != d.end(); it++ ) {
        string& str = *it;
        i = j = 0;
        // Check is sub-sequence-string
        while ( i < s.size() && j < str.size() ) {
            if ( s[ i ] == str[ j ] )
                j++;
            i++;
        }
        // Update longest string
        if ( j == str.size() ) {
            if ( ans.size() == 0 )
                ans = str;
            else if ( cmp( ans, str ) )
                ans = str;
        }
    }
    return ans;
}