#!/usr/bin/env python
#
# written by @jackspp


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        w, h = len(M[0]), len(M)
        ans = copy.deepcopy(M)
        for hi in range(h):
            for wi in range(w):
                gh_max = min(hi+1, h-1)
                gh_min = max(0, hi-1)
                gw_max = min(wi+1, w-1)
                gw_min = max(0, wi-1)

                sum_ = 0
                cnt = 0
                for gh in range(gh_min, gh_max+1):
                    for gw in range(gw_min, gw_max+1):
                        cnt += 1
                        sum_ += M[gh][gw]
                avg = int(sum_ / cnt)
                ans[hi][wi] = avg
        return ans
