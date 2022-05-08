# Practice code added by jmcio 5/5/2022


class SNode (object):
    def __init__(self, data_item=None, next_node=None):
        self.item_ = data_item
        self.next_ = next_node

    def get_item(self):
        return self.item_

    def set_item(self, data_item):
        self.item_ = data_item

    def get_next(self):
        return self.next_

    def set_next(self, next_node=None):
        self.next_ = next_node

    def __str__(self):
        return str(self.item_)

