class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        rst = []
        if target == 0:
            return [[]]

        for cand in candidates:
            if cand > target:
                continue
            fnd_rst = self.combinationSum(candidates, target - cand)
            if fnd_rst != []:
                wanted = [ext + [cand] for ext in fnd_rst]
                for w in wanted:
                    w.sort()
                    if not w in rst:
                        rst.append(w)
        return rst
