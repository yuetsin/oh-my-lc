    public bool IsPalindrome(ListNode head) {
        ListNode t = head;
        ListNode h = head;
        
		// run
        while (h != null) {
            t = t.next;
            h = h.next?.next;
        }
        
        // when hare at finish, tortoise is exactly half way
        
        // since h is null, t now is a finish of right half - I'm just starting to reverse the right half here
        // h is now just previous node to help in reversing
        
        while (t != null) {
            var next = t.next;
            t.next = h;
            h = t;
            t = next;
        }
        
        // now we have 2 lists "head" and "h" and h is shorter or equal
        while (h != null) {
            if (h.val != head.val) {
                return false;
            }
            // promote both nodes
            head = head.next;
            h = h.next;
        }
        return true;
    }