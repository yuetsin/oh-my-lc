class Solution {
public:
    double myPow(double x, long n) {
        if (n < 0) {
            n = -n;
            x = 1 / x;
        }
        double p = 1;
        while (n) {
            if (n & 1) {
                p *= x;
            }
            x *= x;
            n >>= 1;
        }
        return p;
    }
};