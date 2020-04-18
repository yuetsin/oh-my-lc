object Solution {
    def kthGrammar(N: Int, K: Int): Int = {
        if (N == 1) return 0
        if (K % 2 == 0) return if (kthGrammar(N - 1, K / 2) == 0) 1 else 0
        return kthGrammar(N - 1, (K + 1) / 2)
    }
}