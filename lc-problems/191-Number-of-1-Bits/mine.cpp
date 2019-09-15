class Solution {
public:
    int hammingWeight( uint32_t n ) {
        unsigned int c = 0;  // 计数器
        while ( n > 0 ) {
            if ( ( n & 1 ) == 1 )  // 当前位是1
                ++c;               // 计数器加1
            n >>= 1;               // 移位
        }
        return c;
    }
};