int next(int row, unsigned int vertMask, unsigned int leftMask, unsigned int rightMask, unsigned int rangeMask) {
    if (row == 0)
        return 1;
        
    unsigned int mask = rangeMask & ~(leftMask | rightMask | vertMask);
    int r = 0;
    while (mask) {
        unsigned int queenFlag = mask & -mask;
        r += next(
                row-1, 
                (  vertMask | queenFlag ), 
                (  leftMask | queenFlag ) << 1, 
                ( rightMask | queenFlag ) >> 1, 
                rangeMask
            );
        mask ^= queenFlag;
    }
    return r;
}

int totalNQueens(int n) {
    return next(n, 0, 0, 0, ((unsigned int)-1) >> (32-n));
}