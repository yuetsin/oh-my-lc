class Solution {
public:
    double myPow(double x, long n) {
        if (!n) {
            return 1.;
        }
        if (n < 0) {
            return 1.0 / myPow(x, -n);
        }
        if (n % 2) {
            return x * myPow(x, n - 1);
        }
        return myPow(x * x, n / 2);
    }
};