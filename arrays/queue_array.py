#  Practice code added by jmcio 5/8/2022
#  Implement a queue with fixed-size array


class MyCircularQueue():
    def __init__(self, item_count=0, read_index=-1, write_index=-1):
        self.queue = [None] * item_count
        self.read_ = read_index
        self.write_ = write_index
        self.items_ = item_count

    def enqueue(self, item_value):
        if (self.write_ + 1) % self.items_ == self.read_:
            print("Circular Queue is full.\n")
        elif self.read_ == -1:
            self.read_ = self.write_ = 0
            self.queue[self.write_] = item_value
        else:
            self.write_ = (self.write_ + 1) % self.items_
            self.queue[self.write_] = item_value

    def dequeue(self):
        if self.read_ == -1:
            print("The circular queue is empty.\n")
        elif self.read_ == self.write_:
            temp = self.queue[self.read_]
            self.read_ = self.write_ = -1
            return temp
        else:
            temp = self.queue[self.read_]
            self.read_ = (self.read_ + 1) % self.items_
            return temp

    def print_c_queue(self):
        if self.read_ == -1:
            print("No element in the circular queue.\n")
        elif self.write_ >= self.read_:
            for i in range(self.read_, self.write_ + 1):
                print(self.queue[i], end=",")
            print()
        else:
            for i in range(self.read_, self.items_):
                print(self.queue[i], end=",")
            for i in range(0, self.write_ + 1):
                print(self.queue[i], end=",")
            print()


obj = MyCircularQueue(5)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(7)
print("Initial queue...")
obj.print_c_queue()

print("After removing an element from the queue...: ", obj.dequeue())
obj.print_c_queue()
print("After removing an element from the queue...: ", obj.dequeue())
obj.print_c_queue()
print("After removing an element from the queue...: ", obj.dequeue())
obj.print_c_queue()
print("After removing an element from the queue...: ", obj.dequeue())
obj.print_c_queue()
print("After removing an element from the queue...: ", obj.dequeue())
obj.print_c_queue()
