// Instead of checking whether the rectangles overlap, I max right with left( and top with bottom ) .Haven't seen that in other solutions.

int computeArea( int A, int B, int C, int D, int E, int F, int G, int H ) {
    int left = max( A, E ), right = max( min( C, G ), left );
    int bottom = max( B, F ), top = max( min( D, H ), bottom );
    return ( C - A ) * ( D - B ) - ( right - left ) * ( top - bottom ) + ( G - E ) * ( H - F );
}