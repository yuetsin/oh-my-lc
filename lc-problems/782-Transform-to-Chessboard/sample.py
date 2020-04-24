#!/usr/bin/env python

import math

class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rp, cp = board[0], [x[0] for x in board]    #<1>
        rn, cn = [(x+1)%2 for x in rp], [(x+1)%2 for x in cp]   #<2>
        
        def core(is_row): # <3>
            count = errs = 0
            for i in range(N):
                if is_row: line, pos, neg = board[i], rp, rn
                else: line, pos, neg = [x[i] for x in board], cp, cn
                
                if line == pos:
                    count+=1 # <4>
                    if i%2==1: errs+=1  # <A>
                elif line == neg:
                    if i%2==0: errs+=1  # <A>
                else: return -1 # <5>
            if count > math.ceil(N/2) or count < math.floor(N/2): return -1 # <6>
            cand1 = math.inf if errs%2==1 else errs//2  # <B>
            cand2 = math.inf if (N-errs)%2==1 else (N-errs)//2  # <B>
            return min(cand1, cand2) if min(cand1, cand2) != math.inf else -1

        row_ans = core(True)
        if row_ans == -1: return -1
        col_ans = core(False)
        if col_ans == -1: return -1
        return row_ans + col_ans