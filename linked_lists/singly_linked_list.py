# Practice code added by jmcio 5/5/2022


from snode import SNode


class SList(object):
    def __init__(self, head_node=None):
        self.head_ = head_node
        self.size_ = len(self)

    def set_head(self, head_node):
        self.head_ = head_node

    def __len__(self):
        item_count = 0
        current_ptr = self.head_
        while current_ptr:
            item_count += 1
            current_ptr = current_ptr.get_next()
        return item_count

    def __str__(self):
        item_value = ""
        current_ptr = self.head_
        while current_ptr:
            item_value += str(current_ptr)
            current_ptr = current_ptr.get_next()
            if current_ptr is not None:
                item_value += '->'
        return item_value

    def size(self):
        return len(self)

    def empty(self):
        if self.size() != 0:
            return False
        else:
            return True

    def value_at(self, index_value):
        item_count = 0
        current_ptr = self.head_
        while current_ptr:
            if item_count == index_value:
                return current_ptr.get_item()
            else:
                item_count += 1
            current_ptr = current_ptr.get_next()

    def push_front(self, item_value):
        insert_node = SNode(item_value)
        insert_node.set_next(self.head_)
        self.set_head(insert_node)
        return insert_node.get_item()

    def pop_front(self):
        current_ptr = self.head_
        self.head_ = current_ptr.get_next()
        return current_ptr.get_item()

    def push_back(self, item_value):
        insert_node = SNode(item_value)
        current_ptr = self.head_
        if current_ptr is None:
            self.set_head(insert_node)
            return insert_node
        while current_ptr:
            if current_ptr.get_next() is None:
                current_ptr.set_next(insert_node)
                break
            current_ptr = current_ptr.get_next()
        return insert_node

    def pop_back(self):
        current_ptr = self.head_
        prev_ptr = None
        while current_ptr:
            if current_ptr.get_next() is None:
                prev_ptr.set_next(None)
                return current_ptr.get_item()
            prev_ptr = current_ptr
            current_ptr = current_ptr.get_next()

    def front(self):
        current_ptr = self.head_
        return current_ptr.get_item()

    def back(self):
        current_ptr = self.head_
        while current_ptr:
            if current_ptr.get_next() is None:
                return current_ptr.get_item()
            current_ptr = current_ptr.get_next()

    def insert_before(self, index_value, item_value):
        insert_node = SNode(item_value)
        item_count = 0
        current_ptr = self.head_
        prev_ptr = None
        while current_ptr:
            if item_count == index_value:
                insert_node.set_next(current_ptr)
                if index_value == 0:
                    self.set_head(insert_node)
                else:
                    prev_ptr.set_next(insert_node)
                return insert_node.get_item()
            else:
                item_count += 1
            prev_ptr = current_ptr
            current_ptr = current_ptr.get_next()
        raise IndexError("Unable to insert before index, out of bounds.")

    def erase(self, index_value):
        item_count = 0
        current_ptr = self.head_
        prev_ptr = None
        while current_ptr:
            if item_count == index_value:
                if index_value == 0:
                    return self.pop_front()
                prev_ptr.set_next(current_ptr.get_next())
                return current_ptr.get_item()
            else:
                item_count += 1
            prev_ptr = current_ptr
            current_ptr = current_ptr.get_next()

    def remove_value(self, item_value):
        current_ptr = self.head_
        prev_ptr = None
        while current_ptr:
            if current_ptr.get_item() == item_value:
                prev_ptr.set_next(current_ptr.get_next())
                return current_ptr.get_item()
            else:
                prev_ptr = current_ptr
                current_ptr = current_ptr.get_next()

    def value_n_from_end(self, index_value):
        item_count = 0
        current_ptr = self.head_
        while current_ptr:
            if item_count == self.size() - index_value - 1:
                return current_ptr.get_item()
            else:
                item_count += 1
            current_ptr = current_ptr.get_next()

    def reverse(self, head_node=None):
        current_ptr = head_node or self.head_
        new_head = SNode()
        new_head = None
        while current_ptr:
            next_node = SNode()
            next_node = current_ptr.get_next()
            current_ptr.set_next(new_head)
            new_head = current_ptr
            current_ptr = next_node
        if not head_node:
            self.set_head(new_head)
        return new_head


class STList(object):
    def __init__(self, head_node=None, tail_node=None):
        self.head_ = head_node
        self.tail_ = tail_node

    def set_head(self, head_node):
        self.head_ = head_node

    def set_tail(self, tail_node):
        self.tail_ = tail_node

    def __len__(self):
        item_count = 0
        current_ptr = self.head_
        while current_ptr:
            item_count += 1
            current_ptr = current_ptr.get_next()
        return item_count

    def __str__(self):
        item_value = ""
        current_ptr = self.head_
        while current_ptr:
            item_value += str(current_ptr)
            current_ptr = current_ptr.get_next()
            if current_ptr is not None:
                item_value += '->'
        return item_value

    def size(self):
        return len(self)

    def is_empty(self):
        if self.head_:
            return False
        else:
            return True

    def push(self, insert_node):
        if insert_node is not object:
            insert_node = SNode(insert_node)
        insert_node.set_next(self.head_)
        if not self.head_:
            self.set_tail(insert_node)
        self.set_head(insert_node)
        return insert_node

    def append(self, insert_node):
        if not self.head_:
            self.push(insert_node)
            return insert_node
        if insert_node is not object:
            insert_node = SNode(insert_node)
        self.tail_.set_next(insert_node)
        insert_node.set_next()
        self.set_tail(insert_node)
        return insert_node

    def pop(self):
        current_ptr = self.head_
        if current_ptr:
            self.head_ = self.head_.get_next()
            return current_ptr
        else:
            raise IndexError("Unable to pop from empty list")

    def enqueue(self, item_value):
        return self.append(item_value)

    def dequeue(self):
        return self.pop()

    def empty(self):
        while not self.is_empty():
            self.dequeue()
