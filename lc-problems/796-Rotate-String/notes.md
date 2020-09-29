# LC.796

> Rotate String

我记得之前这种字符串操作是叫做 Pivot String 的（

长度 100，实在是太短了，所以我这么白痴的解法也能通过。

Runtime: 32 ms, faster than 48.90% of Python3 online submissions forRotate String.

Memory Usage: 14.1 MB, less than 5.05% of Python3 online submissions for Rotate String.

实际上，因为字符串内部不存在相关性，因此 $O(n)$ 是必然的；不可能有比这更快的算法。

> 只不过…我这个虽然也是 $O(n)$……但是系数…有点大…

KMP（Knuth-Morris-Pratt）的算法转而判断：A + A 是否完全包含了字符串 B。

这样可以避免掉频繁的「字符串拼接」操作，拼接一次多次利用。

但…也不是什么 Amazing 的解法好了。