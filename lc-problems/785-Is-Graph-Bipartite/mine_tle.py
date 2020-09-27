class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        left_ring, right_ring = set(), set()
        
        def try_color(index: int, left_ring: set, right_ring: set) -> bool:
            i = index
            
            if index >= len(graph):
                # done!
                return True
            # iset = set(graph[i])

            may_be_in_left_ring = True
            may_be_in_right_ring = True
            for elem in graph[i]:
                if elem in left_ring:
                    may_be_in_left_ring = False

                if elem in right_ring:
                    may_be_in_right_ring = False
            
            # print(i, "maybe in left?", may_be_in_left_ring, "or right?", may_be_in_right_ring)
            if not (may_be_in_left_ring or may_be_in_right_ring):
                return False
            elif may_be_in_left_ring and may_be_in_right_ring:
                return try_color(index + 1, left_ring, right_ring.union(set([i]))) or try_color(index + 1, left_ring.union(set([i])), right_ring)
            elif may_be_in_right_ring:
                return try_color(index + 1, left_ring, right_ring.union(set([i])))
            elif may_be_in_left_ring:
                return try_color(index + 1, left_ring.union(set([i])), right_ring)

        return try_color(0, set(), set())