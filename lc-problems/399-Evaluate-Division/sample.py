from collections import defaultdict, deque


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        lookup = defaultdict(list)
        for e, v in zip(equations, values):
            num = e[0]
            den = e[1]
            lookup[num].append((den, v))
            lookup[den].append((num, 1/v))

        def bfs(num, den):
            if num not in lookup or den not in lookup:
                return -1

            q = deque([(num, 1)])
            seen = set()
            while len(q):
                curr_node, curr_val = q.pop()
                if curr_node == den:
                    return curr_val
                seen.add(curr_node)
                children = [(x, v*curr_val)
                            for x, v in lookup[curr_node] if x not in seen]
                q.extendleft(children)
            return -1

        ans = []
        for q in queries:
            ans.append(bfs(q[0], q[1]))
        return ans
