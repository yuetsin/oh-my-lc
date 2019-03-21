class Solution {
	fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
		return addTwoNumbersHelper(l1, l2, 0)
	}

	fun addTwoNumbersHelper(l1: ListNode?, l2: ListNode?, overflow: Int): ListNode? {
		var result: ListNode? = null
		if (l1 != null && l2 != null) {
			val sum = l1.`val` + l2.`val` + overflow
			result = ListNode(sum % 10)
			result.next = addTwoNumbersHelper(l1.next, l2.next, sum / 10)
		} else if (l1 != null) {
			val sum = l1.`val` + overflow
			result = ListNode(sum % 10)
			result.next = addTwoNumbersHelper(l1.next, null, sum / 10)
		} else if (l2 != null) {
			val sum = l2.`val` + overflow
			result = ListNode(sum % 10)
			result.next = addTwoNumbersHelper(null, l2.next, sum / 10)
		} else if (overflow == 1) {
			return ListNode(1)
		}
		return result
	}
}