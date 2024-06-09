# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def linked_list_to_int(node):
    num = 0
    place = 1
    while node:
        num += node.val * place
        place *= 10
        node = node.next
    return num

def int_to_linked_list(number):
    dummy = ListNode()
    current = dummy
    if number == 0:
        return ListNode(0)
    while number > 0:
        number, digit = divmod(number, 10)
        current.next = ListNode(digit)
        current = current.next
    return dummy.next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = linked_list_to_int(l1)
        num2 = linked_list_to_int(l2)
        total = num1 + num2
        return int_to_linked_list(total)


# Helper function to create a linked list from a list of integers
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next
