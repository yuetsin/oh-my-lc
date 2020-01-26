#!/usr/bin/env python

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        pass2s = [-1]*(len(s2) + 1) # pass2s[i]: i pass1 can make pass2s[i] passes of pass2
        index2s = [-1]*(len(s2) + 1) # index2s[i]: i pass1 match up to (not including) the pass2s[i] character of S2; all values in index2s should be different, otherwise we will catch the same value and return, as seen in the code below
		# initially without any pass S1:
        pass2s[0] = index2s[0] = 0
        index2 = 0
        pass2 = 0
        for pass1 in range(1, n1+1): # this outer loop will break within min(n1, n2) iterations
            for index1 in range(len(s1)): # use current pass of S1 to match as many characters in S2 as we can
                if s1[index1] == s2[index2]:
                    index2 += 1
                    if index2 == len(s2):
                        index2 = 0
                        pass2 += 1
			# now we know at pass1, how many pass2 we can make, and what the final stopping character
            index2s[pass1] = index2
            pass2s[pass1] = pass2
			
            # detect repeating pattern
            for i in range(pass1): # try fo find one prevous pass1 that can stop at the same character
                if index2s[i] == index2:
					# now we'd like to match index^th character of S2, and we find that one previous pass1, i.e. the i^th pass, can already match that, then the repeating pattern is detected
                    repeating_counts, remain = divmod(n1 - i, pass1 - i)
                    ans = repeating_counts * (pass2s[pass1]-pass2s[i])
                    ans += pass2s[i + remain]
					# ans here means that we can make ans passes of S2
                    return ans // n2
		# if repeating pattern found, then just use all passes of S1, i.e. n1 to make S2
        return pass2s[n1] // n2
