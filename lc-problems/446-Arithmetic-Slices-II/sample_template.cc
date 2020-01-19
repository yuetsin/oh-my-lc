#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;

template < class F >

struct recursive {
    F                                         f;
    template < class... Ts > decltype( auto ) operator()( Ts&&... ts ) const {
        return f( std::ref( *this ), std::forward< Ts >( ts )... );
    }

    template < class... Ts > decltype( auto ) operator()( Ts&&... ts ) {
        return f( std::ref( *this ), std::forward< Ts >( ts )... );
    }
};

template < class F > recursive( F )->recursive< F >;
auto const rec = []( auto f ) { return recursive{ std::move( f ) }; };

class Solution {
public:
    int numberOfArithmeticSlices( vector< int >& A ) {
        using int64 = long long;
        const int n = size( A );

        const auto value_index_map = [&]( unordered_map< int, vector< int > > self = {} ) {
            for ( int i = 0; i < n; ++i )
                self[ A[ i ] ].emplace_back( i );
            return self;
        }();

        auto f = rec( [&, memo = array< gp_hash_table< int64, optional< int > >, 1000 >{}]( auto&& f, int i, int64 d ) mutable -> int {
            if ( memo[ i ][ d ] )
                return *memo[ i ][ d ];
            return *( memo[ i ][ d ] = [&] {
                if ( A[ i ] + d > INT_MAX or A[ i ] + d < INT_MIN or value_index_map.find( ( int64 )A[ i ] + d ) == end( value_index_map ) )
                    return 0;
                int acc = 0;
                for ( const auto& j : value_index_map.at( A[ i ] + d ) )
                    if ( j > i )
                        acc += f( j, d ) + 1;
                return acc;
            }() );
        } );

        auto solution = [&]( int acc = 0 ) {
            for ( int i = 0; i < n; ++i )
                for ( int j = i + 1; j < n; ++j )
                    acc += f( j, int64( A[ j ] ) - A[ i ] );
            return acc;
        };

        return solution();
    }
};