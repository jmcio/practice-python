#  Practice code added by jmcio 5/8/2022
#  Implement a queue with fixed-size array


class Queue(list):
    def __init__(self, item_count=0, read_index=0, write_index=0):
        super().__init__()
        self.read_ = read_index
        self.write_ = write_index
        self.items_ = item_count

    def enqueue(self, item_value):
        if self.write_ == self.read_ and len(self):
            raise IndexError("Unable to enqueue due to buffer write.")
        if self.write_ >= self.read_:
            self.append(item_value)
        else:
            self[self.write_] = item_value
        if self.write_ == self.items_ - 1:
            self.write_ = 0
        else:
            self.write_ += 1
        return self

    def dequeue(self):
        item_value = self.pop(self.read_)
        self.read_ += 1
        return item_value

    def empty(self):
        while self.read_ != self.write_:
            self.dequeue()
