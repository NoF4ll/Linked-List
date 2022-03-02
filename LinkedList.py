from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, new_node) -> object:
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node

        else:
            self.head = new_node

    def delete(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print('Null')

    def length(self):
        temp_node = self.head
        i = 0
        while temp_node:
            i = i + 1
            temp_node = temp_node.next
        return i

    def min(self):
        last_node = self.head
        min_temp = last_node.data
        while last_node.next != None:
            last_node = last_node.next
            if min_temp > last_node.data:
                 min_temp = last_node.data
        return min_temp

    def max(self):
        last_node = self.head
        max_temp = last_node.data
        while last_node.next != None:
            last_node = last_node.next
            if max_temp < last_node.data:
                 max_temp = last_node.data
        return max_temp

    def bubble_sort(self):
        if self.head:
            current = None
            status = 1
            while status == 1:
                status = 0
                current = self.head
                while current and current.next:

                    if current.data > current.next.data:
                        current.data = current.data + current.next.data

                        current.next.data = current.data - current.next.data

                        current.data = current.data - current.next.data
                        status = 1

                    current = current.next

        else:
            print("Empty Linked list")

    def insertionSort(self):

        # Initialize sorted linked list
        sorted = None

        # Traverse the given linked list and insert every
        # node to sorted
        current = self.head
        while (current != None):
            # Store next for next iteration
            next = current.next

            # insert current in sorted linked list
            sorted = sortedInsert(sorted, current)

            # Update current
            current = next

        # Update head_ref to point to sorted linked list
        head_ref = sorted
        return head_ref


def sortedInsert(head_ref, new_node):
    current = None

    # Special case for the head end */
    if (head_ref == None or (head_ref).data >= new_node.data):

        new_node.next = head_ref
        head_ref = new_node

    else:

        # Locate the node before the point of insertion
        current = head_ref
        while (current.next != None and
               current.next.data < new_node.data):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return head_ref