# 2 Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


## Thoughts and Approaches

The most important thing is, inside the while loop, we need to create a list node first for the summed linked list EVERY TIME.

Key Edge Cases to Watch Out ForBefore writing code, you must account for these scenarios:
* Lists of unequal lengths: e.g., $99 + 9$. One list runs out of nodes before the other.
* The Final Carry: e.g., $9 + 9 = 18$. Both lists are exhausted, but you still have a leftover carry of 1 that requires creating a brand new node at the very end.
* Zeros: Input lists like [0] and [0].

## Python Code

```Python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current=dummy=ListNode(0) ## create the first node as the begi of empty linked list
                                 ## Use Current as a pointer, Keep Dummy Stay There!
        carry=0
        s=0  ## define s as the sum of the three parts: 

        while l1 or l2 or carry>0:
            s=carry ##s=carry is put inside the while loop to make sure s is updated with carrry

            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next

            ##IMPORTANT: create a listnode first for the summed linked list
            current.next=ListNode(s%10)  ## in this way, i created a node with value
            current=current.next ## I then move the pointer to current.next
            carry=s//10
        return dummy.next ## dummy.next is the headnode of the the summed linked list
```

## Time Complexity
O(max(m,n)) Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

## Space Complexity
 O(1). The length of the new list is at most max(m,n)+1 However, we don't count the answer as part of the space complexity.

