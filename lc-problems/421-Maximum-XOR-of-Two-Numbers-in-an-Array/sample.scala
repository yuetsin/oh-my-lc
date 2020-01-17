/*
	对每一个元素都在数组内找到异或值最大的那个
    意味着需要从高位到低位找到差异最大的那个
    位越高权重越大，
    且最高位的产生的差异大于余下所有位产生的差异

    2^30 > 2^0 + ... + 2^29

    Trie 字典前缀树存每一位
    高位到低位 1 往左走 0 往右走

                 0           Node(0,0)
(边权重)16      /            /
              1            Node(1,0)
        8   /               /     \
            11          Node(2,0)  Node(1,2) -- 24(110)
        4    \               \        \
              110           Node(0,3)   ...
        2       \             \
               1100           Node(0,4)
        1      /              /
             11001        Node(5,0)

       16 + 8 + 1 = 25

    2^0 + 2^1 + ... + 2^30 个节点

    构建好以后，
    找每个x对应可以异或值最大的那个
    对于每一个x,每次往x路径的不同方向走
*/
object Solution {
    def findMaximumXOR(nums: Array[Int]): Int = {
        case class Node(son:Array[Int]){
      override def toString: String = son.map(_.toString).reduce(_ + _)
    }
    val nodes = scala.collection.mutable.ArrayBuffer[Node]()
    nodes += Node(Array(0,0)) //root
    //construct
    nums.foreach(x => {
      var pos = 0
      (0 to 30).reverse.foreach(i => {
        val curBit = x >> i & 1
        // curBit of the number has no node in trie
        if(nodes(pos).son(curBit) == 0){
          //add an empty node for next bit
          nodes += Node(Array(0,0))
          //current son get the latest path of the number
          nodes(pos).son(curBit) = nodes.length - 1
        }
        // pos get ready for next bit
        pos = nodes(pos).son(curBit)
      })
    })

    // fine the correspond number of current number that can get the Max XOR
    val xors = nums.map(x => {
      var pos,xor = 0
      //greedy top-down by bits ()
      (0 to 30).reverse.foreach(i => {
        val curBit = x >> i & 1
        val rev = if(curBit == 0) 1 else 0
        // curBit of current number can find the reverse bit from nums
        if(nodes(pos).son(rev) != 0){
          //go to next iteration by another path 
          pos = nodes(pos).son(rev)
          xor += 1 << i
        }
        else
        // can not find , go to next iteration by original path
          pos = nodes(pos).son(curBit)
      })

      xor
    })
    
    xors.max
    }
}