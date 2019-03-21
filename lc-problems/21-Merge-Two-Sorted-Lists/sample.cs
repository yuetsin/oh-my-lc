public class Solution 
{
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) 
    {
        var result = new ListNode(int.MinValue);

        for (ListNode p1 = l1, p2 = l2, current = result; current != null;)
        {
            if (p1 != null && (p2 == null || p1.val < p2.val))
            {
                current.next = p1;
                current = p1;
                p1 = p1.next;                
            }
            else if (p2 != null)
            {
                current.next = p2;
                current = p2;
                p2 = p2.next;
            }
            else
            {
                break;
            }
        }
        
        return result.next;        
    }
}