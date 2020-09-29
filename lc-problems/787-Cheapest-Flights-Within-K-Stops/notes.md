# LC.787

> Cheapest Flights Within K Stops

给出一张有向、有权图。要求在不停靠超过 $K$ 次的情况下，从起点到终点的最短路径。

这个，直接用了 DFS 搜。

考虑到整个 Cache 表最多只会有 $O(n K)$ 大小，因此总的时间复杂度不会很差。

Runtime: 292 ms, faster than 11.91% of Python3 online submissions forCheapest Flights Within K Stops.

Memory Usage: 15.6 MB, less than 55.81% of Python3 online submissions for Cheapest Flights Within K Stops.

这题如果用广搜会更合适（想一想你今天上午写的 BFS 连连看）。