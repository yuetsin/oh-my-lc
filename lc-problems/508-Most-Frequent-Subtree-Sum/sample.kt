class Solution {
    fun findFrequentTreeSum(root: TreeNode?): IntArray {
        val subtreeSums = calcSubtreeSums(root).second
        val largestFreq = subtreeSums.values.max()?: return intArrayOf()
        return subtreeSums.filter { it.value == largestFreq }.map { it.key }.toIntArray()
    }

    private fun calcSubtreeSums(root: TreeNode?): Pair<Map<Int, Int>, Map<Int, Int>> {
        return when {
            root == null -> Pair(emptyMap(), emptyMap())
            root.left == null && root.right == null -> {
                val rootSubtreeSums = hashMapOf(Pair(root.`val`, 1))
                Pair(rootSubtreeSums, rootSubtreeSums)
            }
            root.left == null || root.right == null -> {
                val childSubtreeSums = calcSubtreeSums(if (root.left == null) root.right else root.left)
                val withRootSums = childSubtreeSums.first.map { Pair(it.key + root.`val`, it.value) }.toMap()
                Pair(withRootSums, withRootSums.plus(childSubtreeSums.second))
            }
            else -> {
                val leftSubtreeSums = calcSubtreeSums(root.left)
                val rightSubtreeSums = calcSubtreeSums(root.right)
                val withRootSums = leftSubtreeSums.first.keys.flatMap { left ->
                    rightSubtreeSums.first.keys.map { right ->
                        left + right + root.`val` to leftSubtreeSums.first[left]!! * rightSubtreeSums.first[right]!!
                    }
                }.toMap()
                Pair(withRootSums, withRootSums.plus(leftSubtreeSums.second).plus(rightSubtreeSums.second))
            }
        }
    }

    private fun Map<Int, Int>.plus(other: Map<Int, Int>): Map<Int, Int> {
        return (this.keys + other.keys).map { it to (this[it]?: 0) + (other[it]?: 0) }.toMap()
    }
}