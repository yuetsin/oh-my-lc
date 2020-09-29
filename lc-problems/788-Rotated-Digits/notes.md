# LC.788

> Rotated Digits

简而言之，把某个数字的每个数位都旋转 180 度。如果转完得到一个「合法的」「不一样的」数字，那么就是好数字。否则，如果转完等于自己，或者不是一个数字，那么就放弃。

这个，太简单了…

统计一下每个数位出现的频率，分为三类：2569 为一类；018 为二类；347 为三类。

如果出现了 347，直接否决；不是好数字。

再看其中如果没有 2569，也否决；转完了还是自己。

最後得到结果。很简单吧。

Runtime: 88 ms, faster than 64.92% of Python3 online submissions forRotated Digits.

Memory Usage: 15.1 MB, less than 5.13% of Python3 online submissions for Rotated Digits.