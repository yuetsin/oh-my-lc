#!/usr/bin/env python


class Solution(object):
    def predictPartyVictory(self, senate):
        q, bans, cc = collections.deque(list(senate)), {
            'R': 0, 'D': 0}, collections.Counter(senate)
        while(q):
            l = len(q)
            for _ in range(l):
                self.f(bans, q, cc)
            if cc['R'] <= bans['R'] and cc['D']:
                return 'Dire'
            if cc['D'] <= bans['D'] and cc['R']:
                return 'Radiant'

    """
    q = queue of (in order) next senators
    bans['R'] = number of bans against R
    bans['R'] = 5 means previously 5 D have voted to ban 5 R
    same for bans['D']
    cc is the number of R and D left the next round 
    """

    def f(self, bans, q, cc):
        u = q.popleft()
        cc[u] -= 1
        v = 'R' if u == 'D' else 'D'
        if bans[u] <= 0:
            cc[u] += 1
            q.append(u)
            bans[v] += 1
        else:
            bans[u] -= 1
