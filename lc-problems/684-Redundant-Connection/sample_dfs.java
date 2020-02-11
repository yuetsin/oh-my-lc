class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        if (edges == null || edges.length == 0) return new int[0];
        
        Map<Integer, Set<Integer>> map = buildGraph(edges);

        for (int i = edges.length - 1; i >= 0; i--) {
            int u = edges[i][0]; 
            int v = edges[i][1];

            for (int nei : map.get(v)) {
                Set<Integer> seen = new HashSet<>();
                seen.add(v); // block v
                int[] result = dfs(map, u, v, nei, seen);
                if (result != null) return result;
            }
        }
        
        return new int[0];
    }
    
    int[] dfs(Map<Integer, Set<Integer>> map, int u, int v, int next, Set<Integer> seen) {
        seen.add(next);
        for (int nei : map.get(next)) {
            if (seen.contains(nei)) continue;            
            if (nei == u)
                return new int[]{u, v};
            int[] result = dfs(map, u, v, nei, seen);
            if (result != null) return result;
        }
        return null;
    }
    
    Map<Integer, Set<Integer>> buildGraph(int[][] edges) {
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            Set<Integer> nei = map.getOrDefault(u, new HashSet<>());
            nei.add(v);
            map.put(u, nei);

            nei = map.getOrDefault(v, new HashSet<>());
            nei.add(u);
            map.put(v, nei);          
        }
        return map;
    }
}