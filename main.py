from LinkedList import LinkedList
from Node import Node
from random import *

if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(10):
        linked_list.insert(Node(randint(1, 100)))

linked_list.display()
print(linked_list.length())

linked_list.bubble_sort()
linked_list.display()
print(linked_list.length())

