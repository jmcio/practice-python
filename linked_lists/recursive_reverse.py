#  Practice code added by jmcio 5/8/2022

from snode import SNode
from singly_linked_list import SList


def reverse(head_node=SNode(), new_head=SNode()):
    if head_node is None:
        return new_head
    next_node = SNode()
    next_node = head_node.get_next()
    head_node.set_next(new_head)
    new_head = head_node
    head_node = next_node
    return reverse(head_node, new_head)


def main():
    list_v = ('j', 'o', 'h', 'n')
    linked_list = SList()
    for i in list_v:
        linked_list.push_back(i)
    head_v = linked_list.head_
    print("Singly linked list: ", linked_list)
    print("Reversed: ", SList(reverse(head_v)))


if __name__ == "__main__":
    main()
