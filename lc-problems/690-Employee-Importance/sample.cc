class Solution {
public:
    int getImportance( vector< Employee* > employees, int id ) {
        // Here adjacency list is already give in the input. So just map it with its respective id
        unordered_map< int, Employee* > adjlist;
        for ( auto emp : employees )
            adjlist[ emp->id ] = emp;
        if ( adjlist.count( id ) == 0 )
            return 0;
        int sum = 0;
        // BFS
        queue< int >               q;
        unordered_map< int, bool > visited;
        visited[ id ] = true;
        q.push( id );
        while ( !q.empty() ) {
            int node = q.front();
            sum      = sum + ( adjlist[ node ]->importance );
            q.pop();
            for ( int neighbour : adjlist[ node ]->subordinates ) {
                if ( !visited[ neighbour ] ) {
                    visited[ neighbour ] = true;
                    q.push( neighbour );
                }
            }
        }
        return sum;
    }
};