class Solution {
public:
    int addDigits( int num ) {

        if ( num % 10 == num ) {
            return num;
        }

        int res  = num % 10;  // last digit of the number
        int rest = num;       // Take the whole number
        rest -= res;          // remove the digit

        rest /= 10;  // Get the first digit

        int next = res + rest;  // Add them together

        int sum = addDigits( next );  // Keep doing this equation till you find the result.

        return sum;
    }
};