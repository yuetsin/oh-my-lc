import scala.collection.mutable

object Solution {
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val s1, s2 = mutable.Stack[ListNode]() // 后进先出,个位的最后进

    // init
    var cur = l1
    while (cur != null) {
      s1.push(cur)
      cur = cur.next
    }

    cur = l2
    while (cur != null) {
      s2.push(cur)
      cur = cur.next
    }

    // loop
    var carry = 0
    var low = ListNode(-99) // `低位`节点
    while (s1.nonEmpty || s2.nonEmpty || carry > 0) {
      if (s1.nonEmpty) carry += s1.pop().x
      if (s2.nonEmpty) carry += s2.pop().x

      low.x = carry % 10
      val high = ListNode(-99) // `高位`节点,dummy
      high.next = low // 十位之后是个位,每次高位节点都指向低位节点
      low = high // move one step
      carry /= 10
    }

    // res
    low.next
  }
}