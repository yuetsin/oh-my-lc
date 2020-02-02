template < class F > struct rec {
    F                                           f;
    template < class... Args > decltype( auto ) operator()( Args&&... args ) const {
        return f( std::ref( *this ), std::forward< Args >( args )... );
    }

    template < class... Args > decltype( auto ) operator()( Args&&... args ) {
        return f( std::ref( *this ), std::forward< Args >( args )... );
    }
};

template < class F > rec( F )->rec< F >;  // deduction guide for rec

class Solution {
public:
    int removeBoxes( vector< int >& boxes ) {
        const int maxn = 100 + 1;
        const int n    = size( boxes );

        auto f = rec{ [&, memo = array< array< array< optional< int >, maxn >, maxn >, maxn >{}]( auto&& f, int i, int j, int k ) mutable -> int {
            if ( memo[ i ][ j ][ k ] )
                return *memo[ i ][ j ][ k ];
            return *( memo[ i ][ j ][ k ] = [&] {
                if ( i == j )
                    return ( k + 1 ) * ( k + 1 );

                auto remove_first = [&] { return ( k + 1 ) * ( k + 1 ) + f( i + 1, j, 0 ); };

                auto remove_middle = [&]( int acc = INT_MIN ) {
                    for ( int m = i + 1; m <= j; ++m ) {
                        if ( boxes[ i ] == boxes[ m ] and m == j )
                            if ( m > i + 1 )
                                acc = std::max( acc, ( k + 2 ) * ( k + 2 ) + f( i + 1, m - 1, 0 ) );
                            else
                                acc = std::max( acc, ( k + 2 ) * ( k + 2 ) );
                        else if ( boxes[ i ] == boxes[ m ] and m < j )
                            if ( m > i + 1 )
                                acc = std::max( acc, f( i + 1, m - 1, 0 ) + f( m, j, k + 1 ) );
                            else
                                acc = std::max( acc, f( m, j, k + 1 ) );
                    }
                    return acc;
                };

                return std::max( remove_first(), remove_middle() );
            }() );
        } };

        return f( 0, n - 1, 0 );
    }
};