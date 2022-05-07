#  Practice code added by jmcio 5/7/2022

from snode import SNode
from singly_linked_list import SList


def is_palindrome(head_node):
    if head_node is None:
        return True

    fast_node = SNode()
    slow_node = SNode()
    first_half_head = SNode()
    second_half_head = SNode()
    s_list = SList()

    fast_node = head_node
    slow_node = head_node

    while fast_node.get_next() and fast_node.get_next().get_next():
        fast_node = fast_node.get_next().get_next()
        slow_node = slow_node.get_next()

    s_list.set_head(slow_node.get_next())
    second_half_head = s_list.reverse()
    #slow_node.set_next(None)
    first_half_head = head_node

    while second_half_head and first_half_head:
        if first_half_head.get_item() != second_half_head.get_item():
            return False
        second_half_head = second_half_head.get_next()
        first_half_head = first_half_head.get_next()

    return True


def main():
    list_v = (1, 2, 2, 1)
    linked_list = SList()
    for i in list_v:
        linked_list.push_front(i)
    head_v = linked_list.head_
    print("Singly linked list: ", linked_list)
    print("List is a palindrome: ", is_palindrome(head_v))


if __name__ == "__main__":
    main()
