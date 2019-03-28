/*
Runtime: 12 ms, faster than 100.00% of C online submissions for Integer to Roman.
Memory Usage: 7.6 MB, less than 100.00% of C online submissions for Integer to Roman.
*/

char* intToRoman(int num) {
    char* chM[]  = { "", "M", "MM", "MMM" };
    char* chC[]  = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
    char* chX[]  = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
    char* chI[]  = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };
    int   step[] = { 0, 1, 2, 3, 2, 1, 2, 3, 4, 2 };
    char* p      = ( char* )malloc(100);
    memset(p, 0, 100);
    int i   = 0;
    int mod = 0;

    mod   = num / 1000;
    int j = 0;
    for (j = 0; j < step[mod]; j++) {
        *(p + i) = *(chM[mod] + j);
        i++;
    }

    mod = num / 100 % 10;
    for (j = 0; j < step[mod]; j++) {
        *(p + i) = *(chC[mod] + j);
        i++;
    }

    mod = num / 10 % 10;
    for (j = 0; j < step[mod]; j++) {
        *(p + i) = *(chX[mod] + j);
        i++;
    }

    mod = num % 10;
    for (j = 0; j < step[mod]; j++) {
        *(p + i) = *(chI[mod] + j);
        i++;
    }
    return p;
}