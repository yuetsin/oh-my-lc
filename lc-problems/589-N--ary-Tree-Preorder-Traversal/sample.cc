// written by @tjucoder

class Solution {
public:
    vector< int > preorder( Node* root ) {
        deque< Node* > nodes;
        vector< int >  traversal;
        if ( root != nullptr ) {
            nodes.push_front( root );
        }
        while ( !nodes.empty() ) {
            auto cur = nodes.front();
            nodes.pop_front();
            traversal.push_back( cur->val );
            for ( auto iter = cur->children.rbegin(); iter != cur->children.rend(); iter++ ) {
                nodes.push_front( *iter );
            }
        }
        return traversal;
    }
};