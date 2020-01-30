import java.util.*

class Solution {
    fun findBottomLeftValue(root: TreeNode?): Int {
        var leftmost = root!!.`val`
        val queue = LinkedList<TreeNode?>()
        queue.offer(root)
        queue.offer(null)
        while (queue.isNotEmpty()) {
            val node = queue.poll()
            when (node) {
                null -> if (queue.isNotEmpty()) {
                    leftmost = queue.peek()!!.`val`
                    queue.offer(null)
                }
                else -> {
                    node.left?.let { queue.offer(it) }
                    node.right?.let { queue.offer(it) }
                }
            }
        }
        return leftmost
    }
}