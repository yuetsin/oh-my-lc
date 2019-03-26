class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        if target == 0:
            return [[]]
        
        rst = []
        
        for i in range(len(candidates)):
            cand = candidates[i]
            
            if cand > target:
                continue
            
            del candidates[i]
            # print("Removed %d, now candidates = %s" % (cand, str(candidates)))
            fnd_rst = self.combinationSum2(candidates, target - cand)
            candidates.insert(i, cand)
            if fnd_rst != []:
                wanted = [ext + [cand] for ext in fnd_rst]
                for w in wanted:
                    w.sort()
                    if not w in rst:
                        rst.append(w)
            
        return rst