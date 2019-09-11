
static int trailingZeroes( int n ) {
    if ( n < 5 )
        return 0;

    if ( n < 10 )
        return 1;

    return ( n / 5 + trailingZeroes( n / 5 ) );
}