class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t right_ptr = 1, new_val = 0;
        /* unsigned 右移总是会用 0 填充高位 */
        for (int i = 0; i < 16; ++i) {
            new_val |= ((n & right_ptr) << (31 - i * 2));
            right_ptr <<= 1;
        }
        
        for (int i = 16; i < 32; ++i) {
            new_val |= ((n & right_ptr) >> (i * 2 - 31));
            right_ptr <<= 1;
        }
        
        return new_val;
    }
};