from Cython.Compiler.ExprNodes import ListNode


def kthToLast(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: int
    """
    slow = ListNode()
    fast = ListNode()
    slow = fast = head
    while (k > 0):
        k -= 1
        fast = fast.next

    while (fast != None):
        slow = slow.next
        fast = fast.next
    return slow.val

if __name__ == "__main__":
    print(kthToLast([1,2,3,4,5],2))