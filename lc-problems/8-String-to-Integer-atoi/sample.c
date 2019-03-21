#define is_number(ch) (((ch) >= '0') && ((ch) <= '9'))
#define char2number(ch) ((ch) - '0')
/* length of INT32_MIN(or INT32_MAX) */
#define INTMAXLEN 10

int myAtoi(char* str) {
    long long val; /* use long long rather than int */
    int       sign;
    int       len;

    val  = 0;
    sign = 1;
    len  = 0;

    // skip whitespace
    while (*str == ' ') {
        str++;
    }

    // get the sign
    if (*str == '-') {
        sign = -1;
        str++;
    }
    else if (*str == '+') {
        sign = 1;
        str++;
    }
    else if (!is_number(*str)) {
        // first char of non-whitespace characters is not a valid integral number(+, -, 0~9)
        // just return 0
        return 0;
    }

    // skip leading zero
    while (*str == '0') {
        str++;
    }

    // convert string to number
    while (is_number(*str)) {
        val *= 10;
        val += char2number(*str);
        str++;
        len++;
        if (len > INTMAXLEN) {
            // in case `long long` is too small
            // we can just break the loop, so that `long long` won't overflow
            return (sign == -1) ? INT_MIN : INT_MAX;
        }
    }

    // in case that length of `str` equals to INTMAXLEN
    // but its value cannot be held in an int
    if ((val > INT_MAX)) {
        return (sign == -1) ? INT_MIN : INT_MAX;
    }

    return sign * val;
}