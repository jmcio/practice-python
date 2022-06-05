from linked_list import LinkedList
from singly_linked_list import SList, STList
from snode import SNode
from queue_llist import QueueList

#  from node import Node


def main():
    ll = LinkedList()

    print("Initial size: ", len(ll))
    ll.push(24)
    print("New size: ", len(ll))
    print("List content: ", ll)
    print("Pushing more")
    ll.push(6)
    ll.push(783)
    print("List content: ", ll)
    print("popping...")
    ll.pop()
    print("List content: ", ll)
    print("Does list contain 24?")
    if ll.contains(24):
        print("Yes")
    else:
        print("No")
    print("Deleting 24")
    ll.delete(24)
    print("List content: ", ll)
    print("Pushing another onto end.")
    ll.append(365)
    print("List content: ", ll)


def main2():
    slist = SList()
    print("List size: ", slist.size())
    print("Empty check: ", slist.empty())
    print("List contents: ", str(slist))

    # new_v = 'n'
    # print("Push front: ", slist.push_front(new_v))
    #
    # new_v = 'h'
    # print("Push front: ", slist.push_front(new_v))
    #
    # new_v = 'o'
    # print("Push front: ", slist.push_front(new_v))
    #
    # new_v = 'j'
    # print("Push front: ", slist.push_front(new_v))
    #
    # print("List contents: ", str(slist))

    new_v = 2
    print("Push front: ", slist.push_front(new_v))

    new_v = 8
    print("Push front: ", slist.push_front(new_v))

    new_v = 16
    print("Push front: ", slist.push_front(new_v))

    new_v = 32
    print("Push back: ", slist.push_back(new_v))

    print("List contents: ", str(slist))

    # index_v = 1
    # print("Value at index: ", index_v, slist.value_at(index_v))
    #
    # print("Pop front: ", slist.pop_front())
    # print("List size: ", slist.size())
    #
    # new_v = 9
    # print("Push back: ", slist.push_back(new_v))
    # print("List size: ", slist.size())
    #
    # new_v = 11
    # print("Push back: ", slist.push_back(new_v))
    # print("List size: ", slist.size())
    #
    # print("Pop back: ", slist.pop_back())
    # print("List size: ", slist.size())
    #
    # index_v = 1
    # new_v = 23
    # print("Insert before: ", index_v, slist.insert_before(index_v,new_v))
    #
    # index_v = 3
    # new_v = 81
    # print("Insert before: ", index_v, slist.insert_before(index_v,new_v))
    #
    # print("List size....: ", slist.size())
    # print("List contents....: ", str(slist))
    #
#    index_v = 3
#    print("Erase index: ", index_v, slist.erase(index_v))

    # new_v = 81
    # print("Erase value: ", slist.remove_value(new_v))
    print("Reverse list....: ", slist.reverse())

    # index_v = 2
    # print("Value at index: ", index_v, slist.value_n_from_end(index_v))
    #
    # print("Front item: ", slist.front())
    # print("Back item: ", slist.back())
    # print("List size: ", slist.size())
    #
    print("List contents: ", str(slist))
    print("List size: ", slist.size())


def main3():
    ll = QueueList()
    i = SNode(3)
    ll.push(i)
    i = SNode(4)
    ll.append(i)
    i = 5
    print("Enqueue: ", ll.enqueue(i))
    i = 6
    print("Enqueue: ", ll.enqueue(i))
    print("List contents: ", ll)
    print("Head: ", ll.head_)
    print("Tail: ", ll.tail_)
    print("Dequeue: ", ll.dequeue())
    print("List contents: ", ll)
    print("Head: ", ll.head_)
    print("Tail: ", ll.tail_)
    print("Is empty: ", ll.is_empty())
    print("Emptying queue... ")
    ll.empty()
    print("Is empty: ", ll.is_empty())

    ll2 = SList()
    ll2.push_front(i)
    ll2.push_front(SNode(7))
    ll2.push_back(SNode(8))
    print("linked list", ll2.value_at(2))


if __name__ == "__main__":
    main3()
