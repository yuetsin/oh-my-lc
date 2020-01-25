public class CanIWin {
    boolean[] used;
    Map<Integer, Boolean> map;

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;
        if ((maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal) return false;
        used = new boolean[maxChoosableInteger + 1];
        map = new HashMap<>();
        return dfs(desiredTotal);
    }

    private boolean dfs(int desT) {
        if (desT <= 0) return false;
        int key = key();
        if (map.containsKey(key)) return map.get(key);
        for (int i = 1; i < used.length; i++) {
            if (!used[i]) {
                used[i] = true;
                if (!dfs(desT - i)) {
                    map.put(key, true);
                    used[i] = false;
                    return true;
                }
                used[i] = false;
            }
        }
        map.put(key, false);
        return false;
    }

    private int key() {
        int key = 0;
        for (boolean u : used) {
            key <<= 1;
            key |= u ? 1 : 0;
        }
        return key;
    }
}