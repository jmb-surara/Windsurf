# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val   # store the value of this node
        self.next = next # pointer to the next node in the list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # a "dummy head" to simplify building the result list
        current = dummy     # pointer to build the new list
        carry = 0           # carry starts at 0

        # loop while there are nodes left in l1 or l2, or there is a carry
        while l1 or l2 or carry:
            # get the values (0 if the list is already empty)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculate sum of values + carry
            total = val1 + val2 + carry
            carry = total // 10   # new carry (integer division by 10)
            digit = total % 10    # the single digit to store

            # create a new node for the digit
            current.next = ListNode(digit)
            current = current.next

            # move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # skip dummy and return the real head


# -----------------------------
# Helper functions for testing
# -----------------------------
def list_to_linkedlist(numbers):
    """Convert a Python list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# -----------------------------
# Example Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    l1 = list_to_linkedlist([2,4,3])  # represents 342
    l2 = list_to_linkedlist([5,6,4])  # represents 465
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # Expected [7,0,8]

    l1 = list_to_linkedlist([9,9,9,9,9,9,9])  # 9999999
    l2 = list_to_linkedlist([9,9,9,9])        # 9999
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # Expected [8,9,9,9,0,0,0,1]
