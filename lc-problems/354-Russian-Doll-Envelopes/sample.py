#!/usr/bin/env python


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort in one property and find the longest increasing subsequence
        # in the other property, that's it
        # to avoid cases such as [(3, 4), (3, 6)] - output should be 1
        # sort the (w) in ascending and (h) in descending

        # let's sort in second property(h) and then find LIS using first property(w)
        ln = len(envelopes)
        if ln <= 1:
            return ln

        envelopes = sorted(envelopes, key=lambda x: (x[1], -x[0]))
        # now find the LIS
        q = [envelopes[0][0]]

        for i in range(1, ln):
            num = envelopes[i][0]
            if q[-1] < num:
                q.append(num)
            elif q[-1] > num:
                # use binary search
                idx = self.upperbound(q, num)
                q[idx] = num

        return len(q)

    def upperbound(self, ls, num):
        ln = len(ls)
        s, e = 0, ln-1
        while s <= e:
            mid = (e-s)//2 + s
            if ls[mid] == num:
                # we can or we don't have to replace this
                return mid
            elif ls[mid] < num:
                if mid+1 < ln and ls[mid+1] > num:
                    return mid+1
                s = mid + 1
            else:
                if mid == 0:
                    return mid
                e = mid-1
