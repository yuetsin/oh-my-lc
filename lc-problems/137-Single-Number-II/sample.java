  public int singleNumber(int[] nums) {
        int x1 = 0, x2 = 0, x3  = 0, mask = 0;
   
        for (int i : nums) {
            x3 ^= x2 & x1 & i;
            x2 ^= x1 & i;
            x1 ^= i;
            mask = ~(x1 & ~x2 & x3);
            x3 &= mask;
            x2 &= mask;
            x1 &= mask;
        }
        
        return x1;  // Since p = 3, in binary form p = '011', then p1 = p2 = 1, so we can return either x1 or x2. 
                    // If p = 4, in binary form p = '100', only p3 = 1, which implies we can only return x3.
                    // Or alternatively we can simply return (x1 | x2 | x3).
    }