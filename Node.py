from typing import TypeVar

T=TypeVar("T")

class Node:
    def __init__ (self, item) -> T:
        self.item=item
        self.next=None
    
    def get_node_index(self, head, index):
        current=head
        for i in range(index):
            current=current.next
        return current
    def index(self, head, item):
        n=0
        current=head
        while current is not None and current != item:
            current=current.next
            n+=1
        if current is None:
            return ("item not in the linked list")
        return n