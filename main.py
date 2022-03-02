from LinkedList import LinkedList
from Node import Node
from random import *

if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(10):
        linked_list.insert(Node(randint(1, 10)))


    print("Unsortierte Liste:")
    linked_list.display()

    print("Sortierte Liste:")
    linked_list.insertionSort()
    linked_list.display()

    print("Länge der Liste: "+str(linked_list.length()))
    print("Kleinster Wert: "+ str(linked_list.min()))
    print("Größter Wert: "+ str(linked_list.max()))

