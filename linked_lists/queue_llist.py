#  Practice code added by jmcio 5/8/2022
#  Implement a queue with tail pointer


#  from snode import SNode
from singly_linked_list import STList


class QueueList(STList):
    def enqueue(self, item_value):
        return self.append(item_value)

    def dequeue(self):
        return self.pop()

    def empty(self):
        while not self.is_empty():
            self.dequeue()
