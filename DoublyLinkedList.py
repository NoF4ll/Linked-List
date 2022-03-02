from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

#Fügt am Ende ein Neues Node ein
    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last
        return

