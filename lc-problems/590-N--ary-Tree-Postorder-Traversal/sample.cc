// written by @andriy111

class Solution {
public:
    vector< int > postorder( Node* root ) {
        if ( !root )
            return {};
        stack< Node* > s;
        s.push( root );
        vector< int > out;

        while ( !s.empty() ) {
            auto node = s.top();
            s.pop();
            out.push_back( node->val );
            for_each( begin( node->children ), end( node->children ), [&]( auto c ) { s.push( c ); } );
        }
        reverse( begin( out ), end( out ) );
        return out;
    }
};