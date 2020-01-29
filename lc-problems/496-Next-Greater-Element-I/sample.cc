class Solution {
public:
    vector< int > nextGreaterElement( vector< int >& nums1, vector< int >& nums2 ) {
        vector< int >             res;
        stack< int >              s;
        unordered_map< int, int > m;
        for ( int i = nums2.size() - 1; i >= 0; i-- ) {
            while ( !s.empty() && s.top() < nums2[ i ] ) {
                s.pop();
            }
            int ng = ( s.empty() ) ? -1 : s.top();
            m.insert( make_pair( nums2[ i ], ng ) );
            s.push( nums2[ i ] );
        }
        for ( int i = 0; i < nums1.size(); i++ ) {
            res.push_back( m[ nums1[ i ] ] );
        }
        return res;
    }
};