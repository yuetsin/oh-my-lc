class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height) - 1
        def findWaterHeight(x: int) -> int:
            try:
                lmax = max(height[:x])
            except:
                lmax = 0
            try:
                rmax = max(height[x:])
            except:
                rmax = 0
                
            return min(lmax, rmax)
        
        water = 0
        for i in range(width + 1):
            toll = findWaterHeight(i) - height[i]
            water = water + toll if toll > 0 else water
            # print("x = %d, height = %d" % (i, ))
        return water